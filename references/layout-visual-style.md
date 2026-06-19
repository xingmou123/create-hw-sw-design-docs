# Layout And Figure Style Contract

This reference defines the preferred Word layout and engineering-figure taste for Chinese embedded product design documents.

The core principle is: **readability first, restrained engineering aesthetics second, decoration never.**

For this document family, readability means more than clean formatting. The page should feel like a senior engineer is walking a junior engineer through the design: serious internal handoff structure, clear Chinese explanations, visible constraints, concrete recovery paths, and enough reasoning that the reader understands why the system is built this way.

## Non-Negotiable Figure Taste

A final engineering figure should be understandable to a junior engineer in one glance.

Use:

- white background
- no large title inside the image
- no or extremely light shadow
- deep teal for the main path
- light gray for neutral boundaries
- white or very light gray fills for subsystem ownership
- orange only for exception, fallback, or recovery paths
- short Chinese labels
- a small legend only when it reduces confusion
- figure title and long explanation in the Word caption/body, not inside the image

Avoid:

- too many module boxes
- long sentences inside diagrams
- decorative icons
- technology-poster style
- glowing effects
- heavy gradients
- saturated multi-color palettes
- arrows that do not explain the core chain
- repeating body text inside the diagram
- forcing every detail into the architecture figure

## Core Chain Over Module Inventory

The diagram is not a component inventory. It should show the core design route.

For device-App-cloud systems, the first architecture diagram should make the locked route obvious. A common example is:

`控制走 BLE -> 图片走 Wi-Fi HTTP -> AI 走网关 -> 异常回到 IDLE`

If the project route is different, lock that route first, then draw only that route. Never mix two conflicting routes in the same final diagram.

The main architecture figure should answer:

- Who owns control?
- Who owns image payload?
- Who calls AI?
- Where does exception recovery go?

It does not need to show every task, every API, every field, every test, or every driver. Those belong in later mechanism figures, tables, or body text.

## Preferred System Architecture Layout

Use four to five subsystem blocks at most:

- device side
- mobile/App side
- AI gateway
- external model/TTS service
- optional verification/tooling block only when it is essential

Inside each block, keep only 3-5 short module labels.

Good labels:

- `设备端`
- `Android App`
- `AI 网关`
- `云模型服务`
- `BLE 控制`
- `Wi-Fi HTTP 图像`
- `OCR / 问答 / TTS`
- `异常回 IDLE`

Weak labels:

- long explanatory sentences
- implementation paragraphs
- every API route listed in the main figure
- every task/thread listed in the main figure
- every test script listed in the main figure

## Sequence And Table Carry The Detail

When the architecture has more detail than the main figure can carry, split it:

1. Main architecture figure: only subsystem ownership and core routes.
2. Sequence/data-flow figure: numbered runtime steps.
3. Explanation table: design points, constraints, tradeoffs, verification.

This keeps the page professional and readable without turning the main figure into a crowded map.

## State Machine Style

State machine figures should be especially restrained:

- small boxes
- stable spacing
- few arrows
- normal path in deep teal
- exception/recovery path in orange dashed lines
- no long descriptions inside states
- explanatory text below the figure or in body paragraphs

The core should be readable as:

`IDLE -> CAPTURING -> TRANSFERRING -> AI_PROCESSING -> READY -> IDLE`

Exception path:

`TIMEOUT / DISCONNECT / ERROR -> RECOVERING -> IDLE`

Do not draw every theoretical transition if it makes the figure harder to understand.

## Imagegen Workflow For Engineering Diagrams

`imagegen` is mandatory for custom explanatory figures when available, and final engineering diagrams must remain pure imagegen outputs.

Do not replace `imagegen` with local script diagrams. Do not use local drawing or post-processing to correct labels, arrows, cropping, resolution, module boxes, colors, or layout.

The final figure must remain the selected imagegen output. Do not locally redraw text, arrows, modules, icons, or layout. Regenerate and screen instead. Copying the selected image into the project and resizing it in Word is acceptable because it does not change pixels; local engineering correction is not acceptable.

If real hardware photos, product photos, board images, logos, or model-service icons would make a figure clearer, first ask for a user-provided asset or locate an already provided local asset. Keep these real elements restrained and purposeful. Without a real asset, use abstract module boxes rather than hallucinating a specific board or product appearance.

Use strong prompts:

- white background
- no title
- restrained engineering diagram
- no decorative icons
- no glow
- no marketing look
- short labels only
- deep teal main lines
- orange only for exception/fallback/recovery
- few modules
- arrows only for the core chain

Screen generated candidates for:

- wrong or garbled text
- random extra labels
- wrong arrows
- too many boxes
- decorative icons
- poster-like rendering
- inconsistent color meaning
- image title inside the diagram

Maintain an imagegen evidence log:

- figure number
- prompt summary or prompt file
- candidate count
- selected imagegen output path
- final inserted asset path
- SHA-256 of the selected imagegen output
- SHA-256 of the final inserted asset
- rejected reasons
- allowed non-pixel-changing operation, usually `copy only`

If imagegen text or arrows are unreliable, regenerate with shorter labels, move details to Word captions/tables, or ask the user for a source figure or explicit exception. Do not use imagegen only as a style reference and correct the final labels/arrows locally.

When the user asks to optimize, unify, add, or replace figures, the output must include actual changed figure assets and the DOCX must reference those assets. Do not claim visual improvement if the only changes are captions, surrounding text, or prompts that were not used in the final Word file.

## Cover And TOC Page

The cover/TOC page should look like an engineering release document:

- centered product name and document title
- version and delivery status under the title
- compact metadata table
- real Word TOC based on Heading styles
- single-column or two-column TOC chosen by rendered readability
- dotted leaders and page numbers
- simple footer page number
- no marketing graphics

The cover communicates seriousness through structure and spacing, not decoration.

Do not force a two-column TOC when it makes the page cramped. For dense software/hardware design documents, a single-column TOC with clean hierarchy, dotted leaders, right-aligned page numbers, and enough whitespace is often more formal than a squeezed two-column layout. A TOC that spans two pages is acceptable if it reads like a release document rather than a generated index.

## V1.3 Baseline Lesson

Use the V1.3-style sample as a readability and page-composition baseline, not as a final coverage limit.

Preserve:

- centered document title and version
- compact metadata table
- clean revision record
- clean TOC with dotted leaders, page numbers, and readable hierarchy
- deep teal headings and restrained table styling
- system page composition with architecture figure, runtime flow, and explanation table

Improve:

- add more figures when mechanisms are text-only
- keep figure captions in Word, not inside images
- make every custom explanatory figure traceable to imagegen
- avoid accepting sparse hardware documents with only one high-level block diagram
- avoid letting a polished TOC hide weak mechanism coverage

## First System Design Page Pattern

A strong first system-design page can combine:

- section heading
- restrained architecture figure
- compact end-to-end sequence/data-flow figure
- short design explanation table

Do not let the page become sparse, but also do not make the main figure carry all detail. Use the page composition to distribute complexity.
