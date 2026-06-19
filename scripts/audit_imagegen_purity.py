#!/usr/bin/env python3
"""Verify pure-imagegen figure provenance for final DOCX deliverables.

Manifest schema:
{
  "figures": [
    {
      "figure": "图 2-1",
      "kind": "custom_imagegen",
      "selected_imagegen_output": "E:/.../generated_images/.../fig.png",
      "final_asset": "D:/project/assets/figures/fig_2_1.png",
      "allowed_operation": "copy only"
    },
    {
      "figure": "图 A-1",
      "kind": "source_figure",
      "final_asset": "D:/project/assets/photo.png",
      "source_note": "user-provided board photo"
    }
  ]
}

For each custom_imagegen figure:
- selected_imagegen_output and final_asset must be byte-identical.
- final_asset bytes must appear inside at least one provided DOCX word/media/* item.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def docx_media_hashes(docx_paths: list[Path]) -> dict[str, list[str]]:
    hashes: dict[str, list[str]] = {}
    for docx in docx_paths:
        with zipfile.ZipFile(docx) as zf:
            for name in zf.namelist():
                if not name.startswith("word/media/") or name.endswith("/"):
                    continue
                digest = sha256_bytes(zf.read(name))
                hashes.setdefault(digest, []).append(f"{docx}:{name}")
    return hashes


def audit(manifest_path: Path, docx_paths: list[Path]) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    media_hashes = docx_media_hashes(docx_paths)
    results: list[dict[str, Any]] = []
    failed = False

    for item in manifest.get("figures", []):
        kind = item.get("kind", "custom_imagegen")
        result: dict[str, Any] = {
            "figure": item.get("figure"),
            "kind": kind,
            "status": "skipped" if kind != "custom_imagegen" else "pending",
            "messages": [],
        }

        if kind != "custom_imagegen":
            result["messages"].append("non-custom source/user-approved figure; purity check skipped")
            results.append(result)
            continue

        selected = Path(item.get("selected_imagegen_output", ""))
        final = Path(item.get("final_asset", ""))
        allowed = str(item.get("allowed_operation", "")).strip().lower()
        if allowed not in {"copy only", "lossless copy", "word scaling only"}:
            result["messages"].append(f"unexpected allowed_operation: {allowed!r}")
            failed = True

        if not selected.exists():
            result["messages"].append(f"selected_imagegen_output missing: {selected}")
            failed = True
        if not final.exists():
            result["messages"].append(f"final_asset missing: {final}")
            failed = True
        if result["messages"]:
            result["status"] = "failed"
            results.append(result)
            continue

        selected_hash = sha256_file(selected)
        final_hash = sha256_file(final)
        result["selected_sha256"] = selected_hash
        result["final_sha256"] = final_hash
        if selected_hash != final_hash:
            result["messages"].append("final asset is not byte-identical to selected imagegen output")
            failed = True

        media_matches = media_hashes.get(final_hash, [])
        result["docx_media_matches"] = media_matches
        if not media_matches:
            result["messages"].append("final asset bytes were not found in provided DOCX media")
            failed = True

        result["status"] = "passed" if not result["messages"] else "failed"
        results.append(result)

    return {
        "manifest": str(manifest_path),
        "docx": [str(p) for p in docx_paths],
        "figure_count": len(manifest.get("figures", [])),
        "custom_imagegen_count": sum(1 for f in manifest.get("figures", []) if f.get("kind", "custom_imagegen") == "custom_imagegen"),
        "failed": failed,
        "results": results,
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Audit pure-imagegen figure provenance in DOCX deliverables.")
    parser.add_argument("--manifest", required=True, type=Path, help="JSON manifest with selected imagegen outputs and final assets")
    parser.add_argument("docx", nargs="+", type=Path, help="Final DOCX files to inspect")
    args = parser.parse_args(argv)

    result = audit(args.manifest, args.docx)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
