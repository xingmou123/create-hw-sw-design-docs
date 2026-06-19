#!/usr/bin/env python3
"""Audit a DOCX package for headings, tables, drawings, media, and figure captions."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
}


CAPTION_RE = re.compile(r"^\s*(图|Figure)\s*\d+([-.]\d+)?")


def _read_xml(zf: zipfile.ZipFile, name: str) -> ET.Element | None:
    try:
        data = zf.read(name)
    except KeyError:
        return None
    return ET.fromstring(data)


def _paragraph_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.findall(".//w:t", NS)).strip()


def _paragraph_style(p: ET.Element) -> str:
    style = p.find("./w:pPr/w:pStyle", NS)
    if style is None:
        return ""
    return style.attrib.get(f"{{{NS['w']}}}val", "")


def audit_docx(path: Path) -> dict:
    result: dict = {
        "path": str(path),
        "exists": path.exists(),
        "size_bytes": path.stat().st_size if path.exists() else None,
        "is_docx_zip": False,
        "media": [],
        "media_count": 0,
        "drawing_count": 0,
        "picture_count": 0,
        "table_count": 0,
        "paragraph_count": 0,
        "heading_count": 0,
        "headings": [],
        "caption_count": 0,
        "captions": [],
        "warnings": [],
    }

    if not path.exists():
        result["warnings"].append("file does not exist")
        return result

    try:
        with zipfile.ZipFile(path) as zf:
            result["is_docx_zip"] = True
            names = zf.namelist()
            media = [n for n in names if n.startswith("word/media/") and not n.endswith("/")]
            result["media"] = media
            result["media_count"] = len(media)

            root = _read_xml(zf, "word/document.xml")
            if root is None:
                result["warnings"].append("word/document.xml missing")
                return result

            paragraphs = root.findall(".//w:p", NS)
            result["paragraph_count"] = len(paragraphs)
            result["table_count"] = len(root.findall(".//w:tbl", NS))
            result["drawing_count"] = len(root.findall(".//w:drawing", NS))
            result["picture_count"] = len(root.findall(".//pic:pic", NS))

            for p in paragraphs:
                text = _paragraph_text(p)
                if not text:
                    continue
                style = _paragraph_style(p)
                if style.lower().startswith("heading") or style.startswith("标题"):
                    result["headings"].append(text)
                if CAPTION_RE.match(text):
                    result["captions"].append(text)

            result["heading_count"] = len(result["headings"])
            result["caption_count"] = len(result["captions"])

    except zipfile.BadZipFile:
        result["warnings"].append("not a valid docx zip")
    except ET.ParseError as exc:
        result["warnings"].append(f"xml parse error: {exc}")

    if result["media_count"] and result["drawing_count"] == 0:
        result["warnings"].append("media files exist but no drawing nodes found")
    if result["drawing_count"] and result["caption_count"] == 0:
        result["warnings"].append("drawings exist but no figure captions found")

    return result


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Audit a DOCX for delivery checks.")
    parser.add_argument("docx", type=Path)
    parser.add_argument("--min-images", type=int, default=0)
    parser.add_argument("--min-captions", type=int, default=0)
    parser.add_argument("--min-tables", type=int, default=0)
    args = parser.parse_args(argv)

    result = audit_docx(args.docx)

    failed = False
    if args.min_images and result["media_count"] < args.min_images:
        result["warnings"].append(f"media_count below minimum: {result['media_count']} < {args.min_images}")
        failed = True
    if args.min_captions and result["caption_count"] < args.min_captions:
        result["warnings"].append(f"caption_count below minimum: {result['caption_count']} < {args.min_captions}")
        failed = True
    if args.min_tables and result["table_count"] < args.min_tables:
        result["warnings"].append(f"table_count below minimum: {result['table_count']} < {args.min_tables}")
        failed = True
    if not result["exists"] or not result["is_docx_zip"]:
        failed = True

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
