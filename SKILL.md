---
name: create-hw-sw-design-docs
description: Create or revise rigorous Chinese Word/DOCX software detailed design and hardware detailed design documents for embedded, IoT, wearable, robotics, AI hardware, edge-cloud, or hardware-product projects. Use when the user provides a project description, resume material, notes, source code, existing DOCX files, or rough requirements and asks for big-company-style engineering documents, learner-facing project delivery documents, system architecture/design docs, hardware/software detailed design specs, Word deliverables, imagegen architecture figures, or final handoff packages. Default final output must be verified professional .docx files, usually separate software and hardware documents, unless the user explicitly asks for draft text only.
---

# Create HW/SW Design Docs

## Purpose

Turn rough project material into professional engineering Word documents:

- `软件详细设计说明书`
- `硬件详细设计说明书`
- Optional lightweight system overview embedded in both documents, or a separate system design document only when needed

The visible document should read like a restrained project-team handoff document. It should help a learner understand, run, debug, verify, and explain the project, but the document itself must not look like training notes, interview coaching, marketing copy, or AI-generated filler.

For Chinese embedded engineering deliveries, the document must preserve a reader-first engineering style: speak plainly, explain mechanisms deeply, avoid corporate empty phrases, and make a Chinese embedded learner feel the system can be understood and reproduced.

Important: do not use the `lixin-embedded-writer` public-article skill as the writing model for these deliverables. The target is not a公众号 article. Use the user's confirmed engineering-doc readability standard instead: the document should look like an internal engineering handoff, but explain deep design decisions clearly enough that a junior embedded engineer can follow the route, understand the tradeoffs, locate failures, and verify the result.

## Required References

Before drafting, revising, or generating final deliverables, read:

- `references/document-standards.md` for positioning, truth boundaries, writing rules, visual rules, and quality gates.
- `references/output-templates.md` for Word structure, figure plans, recommended software/hardware chapter maps, and required tables.
- `references/layout-visual-style.md` for the restrained cover/TOC layout, figure taste, route clarity, imagegen screening rules, state-machine style, sequence/data-flow style, and explanation-table composition.

When verifying completed `.docx` files, use:

- `scripts/audit_docx.py` to inspect media, drawing nodes, captions, headings, and tables.

## Mandatory Workflow

1. **Lock the engineering boundary**
   - Identify product type, reader, technology stack, canonical route, current evidence, and requested output package.
   - Before drafting, run a user alignment gate. Ask the user to confirm any facts that materially change architecture, maturity language, evidence claims, visual assets, or output package.
   - Use chat text as the default alignment method. If the likely route is clear, ask for one concise confirmation sentence. If a decision has multiple valid routes, present a short numbered option list with 2-3 choices, put the recommended default first, and accept either the option number or free-form user text.
   - Always ask whether the user has real product, board, chip, schematic, screenshot, logo, existing diagram, or reference photo assets to supply before planning final figures. If the user provides files, treat them as authoritative visual assets. If the user declines or does not provide them, use abstract engineering diagrams and state that no physical appearance is claimed.
   - If the material mixes incompatible routes, force the main route before drafting. Do not write two conflicting architectures into one final document.
   - If earlier notes conflict with a later user correction, treat the later correction as the route lock and mark the earlier route as historical/alternative only when it must be mentioned. For device-App-cloud projects, two conflicting payload routes such as `BLE image chunking` and `Wi-Fi HTTP image transfer` must not both appear as the final main route.
   - Lock maturity from the latest user instruction and evidence boundary. If the user asks for a `正式发布` / `量产发布` software or hardware design document, write the document form as `正式发布设计基线` / `正式发布版设计说明书`; keep unsupported factory, certification, self-designed PCB, thermal, EMC/ESD, and production-test claims as `生产导入约束` or `不覆盖范围`. If no maturity is specified, default to evidence-bounded `产品化验证` / `小批量试产验证`.
   - Do not call the project `demo` or `原型玩具` when the user wants product-grade framing.
   - Do not claim completed mass production, factory readiness, EMC/ESD/thermal certification, self-designed PCB, or manufacturing closure without evidence.
   - Separate user-provided facts, verified facts, assumptions, and missing evidence.

2. **Design the document set**
   - Default serious delivery is two separate `.docx` files: software detailed design and hardware detailed design.
   - Use one combined DOCX only for a quick sample or when the user asks for one file.
   - Keep the two documents aligned: same product route, same responsibility boundary, same version language, same figure style.
   - Include system overview in both documents when it helps the reader enter the project before subsystem details.

3. **Build the chapter map from project value**
   - Lead with end-to-end architecture, responsibility boundaries, data/control flow, interfaces, state transitions, exception recovery, design tradeoffs, verification, and residual risks.
   - Avoid generic component encyclopedias, long background sections, decorative market prose, and repeated summaries.
   - Build a real chapter map before writing: include H1/H2/H3 depth, section purpose, required tables, figure placement, and evidence/assumption notes.
   - Do not accept a coarse TOC that only lists broad chapters such as architecture, protocol, test, and risk. A strong TOC should let the reader predict the system route and the engineering depth before reading the body.
   - For each important mechanism, cover: design goal, constraints, chosen design, why this design, failure handling, verification method, and reader takeaway.
   - Source-code mapping tables are optional enhancements, not required structure. Use them when source code is available and the user wants traceability; do not make them mandatory because later projects may have only project descriptions, screenshots, logs, or existing documents.
   - Convert learner/interview goals into normal engineering sections. Do not put headings such as `面试重点`, `快速上手`, `训练路线`, or `核心概念` into final engineering docs unless the user explicitly asks for a training appendix.
   - For Chinese learners/readers, prioritize Chinese readability over internationalized-looking English. Keep protocol names, chip names, APIs, commands, and abbreviations in English only where they are the real technical identifier.

4. **Plan figures before writing final DOCX**
   - Create a figure coverage plan with figure number, target section, purpose, visual type, image generation method, and final caption.
   - Before generating the full document, run an imagegen file-output preflight on one small disposable figure: call the selected imagegen path, then verify that a new image file appeared under `$CODEX_HOME/generated_images/...` or another selected-imagegen output path, and record its path, timestamp, and SHA-256. If no new file is discoverable, stop before DOCX generation and report the imagegen output-path blocker. Do not reuse old generated images.
   - Create an imagegen evidence log before final handoff: figure number, prompt summary, candidate count, selected imagegen output path, final inserted asset path, SHA-256 for both files, rejected reason for bad candidates, and allowed non-pixel-changing operations.
   - If you claim that figures were optimized, unified, regenerated, added, or replaced, there must be actual new/changed image assets and those assets must be inserted into the DOCX. Do not describe figure work as completed when only the text around the figure changed.
   - Pure imagegen is the default and mandatory for this skill's custom explanatory figures. The final inserted asset must be the selected `imagegen` output file itself, with identical bytes or an explicitly documented lossless copy. Word scaling is allowed; changing the pixels is not.
   - For each figure, verify the selected output is newly generated for this task or explicitly carried over from a task-relevant user-approved source. Do not select unrelated historical files from `$CODEX_HOME/generated_images`.
   - Do not substitute deterministic local script diagrams, PIL/canvas diagrams, Mermaid exports, SVG redraws, HTML/canvas screenshots, or hand-built graphics for `imagegen` output.
   - Do not locally redraw or correct labels, arrows, icons, module boxes, layout, colors, cropping, or text on a custom explanatory figure. This is forbidden even when the generated Chinese text is imperfect.
   - If all imagegen candidates fail because of wrong text, wrong arrows, garbled labels, or poor layout, regenerate with shorter labels, move detail into Word captions/tables, or stop and report that the pure-imagegen figure could not be accepted. Do not use a local correction escape hatch.
   - The only non-imagegen visuals allowed in final documents are user-provided or authoritative source figures, schematics, screenshots, measurement charts, or explicit user-approved exceptions. Label these as source figures, not custom explanatory figures.
   - If a figure would benefit from a real board, product, chip, logo, model-service icon, or reference photo, ask the user to upload the asset or identify an existing local file before generating the figure. Use such real visual material sparingly and only where it improves understanding. If the user does not provide a real asset, do not hallucinate a specific physical board/product image.
   - Use white background, restrained engineering colors, short technical labels, clean arrows, no title inside the image, no decorative icons, no glowing “tech” effects.
   - Use Chinese labels by default in figures. English is allowed for real identifiers such as `ESP32-S3`, `BLE GATT`, `PSRAM`, `FastAPI`, `Qwen-VL`, `CRC`, `MTU`, `request_id`, `pytest`, and `ADB`; explanatory words such as module role, flow name, failure path, status, and legend should be Chinese.
   - The main architecture figure must show the core route, not a component inventory. For device-App-cloud projects, a typical route is `控制走 BLE -> 图片走 Wi-Fi HTTP -> AI 走网关 -> 异常回到 IDLE`; use it only when it matches the user's locked route.
   - Keep modules few and precise. Put long explanations, dense fields, and detailed steps into sequence diagrams, tables, or body text instead of the main figure.
   - Put the figure title in the Word caption, not inside the image.
   - Treat a 20+ page software document with only 3-5 figures, or a 12+ page hardware document with only one figure, as under-illustrated for this use case.
   - Treat V1.3-style layout as a useful readability baseline, not a figure-count baseline: preserve the disciplined cover/TOC/page composition, but increase figure coverage when important mechanisms remain text-only.
   - For major system pages, prefer a compound page layout: architecture diagram plus end-to-end sequence/data-flow diagram plus a compact explanation table when space allows. Do not let key design pages feel sparse.

5. **Generate professional Word deliverables**
   - Produce `.docx` files as the final artifact. Do not stop at Markdown unless the user explicitly asked for draft/preview text.
   - Use the session's document/DOCX capability when available. If creating DOCX with code, still verify the final Word package.
   - Include cover page, version record, scope/evidence boundary, Word-compatible TOC, consistent headings, tables, figures, captions, footer/page numbers, and versioned filenames.
   - The cover and TOC should follow an engineering release-document feel: centered title/version, compact metadata table, real Word TOC based on Heading styles, dotted leaders, right-aligned page numbers, and clean hierarchy. Choose single-column or two-column TOC by rendered readability; if a two-column TOC becomes cramped or wraps awkwardly, use a single-column TOC even if it spans multiple pages.
   - Bind Chinese Word fonts explicitly at style and run level: set `ascii`, `hAnsi`, `eastAsia`, and `cs` fonts for Normal, Heading 1/2/3, Caption, TOC, tables, headers, and footers. Do not rely on theme fonts such as `majorEastAsia`.
   - Remove Word paragraph-format flags that show a black square when formatting marks are enabled, especially `keepNext`, `keepLines`, and `pageBreakBefore` on Heading styles and heading paragraphs, unless the user explicitly wants those marks.
   - For serious delivery, optionally package DOCX/PDF/render evidence in a zip.

6. **Verify before final handoff**
   - Open or inspect the DOCX before claiming completion.
   - Perform a three-pass final review before handoff:
     1. Route/truth pass: maturity, evidence boundary, no demo wording, no mass-production inflation, no route contradictions.
     2. Reader pass: Chinese-first readability, mechanism-specific headings, no all-English diagrams, no training/HR/marketing phrasing.
     3. Visual pass: every planned custom explanatory figure exists, every custom figure is a pure imagegen final asset, rejected imagegen failures are not used, captions live in Word, and diagrams follow the restrained visual contract.
   - Run `scripts/audit_docx.py` on each final DOCX and check media count, drawing count, captions, headings, and tables.
   - Run `scripts/audit_imagegen_purity.py` with the imagegen manifest and final DOCX files. The audit must show every custom explanatory DOCX media file matches a selected imagegen output hash. If this audit cannot be run, report the delivery as not pure-imagegen verified.
   - The imagegen purity audit must be run after Word COM or any other DOCX save/update step, because Word updates can rewrite package contents. If any DOCX is modified after the audit, rerun the audit and rebuild the final package.
   - When figure changes were promised, verify the DOCX media inventory changed as expected and report the final figure count and captions. If no figure changed, say so directly and do not claim visual optimization.
   - Run a style audit on each DOCX: Heading 1/2/3 must have no black-square trigger flags (`keepNext`, `keepLines`, `pageBreakBefore`), text runs must not be missing `eastAsia` font binding, and theme font fallback count should be zero.
   - Verify the rendered TOC page itself, not only the heading list. It must show stable hierarchy, dotted leaders, readable spacing, and page numbers. If the visible TOC looks like a rough generated list, the document is not final.
   - Report changed/created files, checks run, figure inventory, and remaining assumptions or risks.

## Intake Rules

Ask only questions that materially affect correctness. If the user says to proceed, make conservative assumptions and label them.

Use questions as an alignment gate, not an endless interview. Batch the important confirmations when possible. Default to normal chat text instead of tool-specific popups so the workflow works in any Codex mode.

Use the simplest interaction that can safely align the work:

- For obvious defaults, ask one compact confirmation: `默认按 A / B / C 继续；如果有实物图片、截图、原理图、BOM 或测试记录，请现在补充。`
- For ambiguous or high-impact decisions, provide 2-3 numbered choices, put the recommended default first, and explain the practical impact of each choice in one sentence.
- Accept user replies by option number, short phrase, or free-form text. If the reply resolves the key boundary, proceed without asking again.
- Do not block on low-impact preferences such as wording taste, minor formatting, or filename style.

Critical questions:

- What is the canonical product route and technology stack?
- Are there source code, existing DOCX files, schematics, BOM, test records, logs, or screenshots to ground the docs?
- Are there real product, board, chip, schematic, screenshot, logo, existing diagram, or reference photo assets that should be used in figures?
- Should output be the default two Word files, a single sample DOCX, PDF export, or a zip package?
- Which facts are verified measurements versus desired claims?
- Is the hardware a module/EVB-based validation platform, a self-designed PCB, or a production-intent board?

## Completion Gate

Do not mark the task complete unless:

- Final output is actual `.docx` files, unless the user explicitly scoped the task to skill editing, outline, or draft text.
- The user alignment gate was completed or explicitly waived, including the physical/reference-image asset question and any high-impact chat confirmations.
- The documents do not pretend to be internal DJI/Huawei/company materials.
- The maturity language follows the user's locked document status while staying evidence-bounded: use `正式发布设计基线` when requested, but do not invent completed factory, certification, self-designed PCB, EMC/ESD, thermal, or production-test closure without proof.
- Software and hardware documents share the same system route and do not contradict each other.
- The TOC/chapter map is not rough: it has meaningful H2/H3 depth, clear engineering progression, table/figure landing points, and no vague filler sections.
- Important architecture, protocol, state, recovery, hardware boundary, and verification sections have meaningful figures.
- The imagegen evidence log exists for custom explanatory figures, and every custom explanatory figure inserted into the DOCX is byte-identical to a selected `imagegen` output or an explicitly documented lossless copy.
- Imagegen file-output preflight succeeded for the current task; no unrelated historical generated image was reused as a selected output.
- Any promised figure optimization is backed by changed image assets, changed DOCX media, and visible inserted figures/captions.
- The document is readable for Chinese embedded learners: Chinese is the primary language, English is limited to real technical identifiers, and diagrams are not English-only.
- For Chinese embedded engineering delivery, the tone is plain, grounded, engineering-focused, and reader-first; it must not read like a generic template, HR copy, marketing brochure, or AI summary.
- All custom figures are pure `imagegen` final assets unless they are user-provided/source figures or an explicitly user-approved exception.
- `scripts/audit_imagegen_purity.py` passes for the final DOCX package, or the handoff states clearly that pure-imagegen verification failed and the deliverable is not final.
- `scripts/audit_imagegen_purity.py` was rerun after the last DOCX modification and before final zip/package creation.
- The DOCX audit confirms images, drawing nodes, captions, headings, and tables exist at the expected level.
- The DOCX style audit confirms no visible black-square paragraph markers on headings when Word formatting marks are enabled, and Chinese text uses a real Chinese font binding such as `Microsoft YaHei` / `微软雅黑` rather than unresolved theme fonts.
- Unsupported numbers are marked as assumptions, targets, or `待实测`.
