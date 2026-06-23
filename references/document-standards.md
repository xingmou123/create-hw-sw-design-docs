# Document Standards

## Core Philosophy

The goal is not to imitate a leaked big-company template. The goal is to produce credible engineering documents that reflect big-company engineering logic:

`需求/规格 -> 系统架构 -> 软硬件详细设计 -> 接口/协议 -> 验证测试 -> 问题闭环 -> 发布交付`

For learner-facing embedded or hardware-product projects, the most valuable final documents are usually:

- `软件详细设计说明书`
- `硬件详细设计说明书`

They should include enough system overview to prevent the reader from falling directly into GPIO, RTOS, BLE, power, or cloud details without understanding the whole product.

The document should make the reader feel:

`这是一个项目组内部交接资料，我按这个能看懂项目、跑通项目、定位问题，也能把项目讲清楚。`

For Chinese embedded engineering delivery, add one more standard:

`像一个真正做过项目、带过学员、见过工程标准的人，在认真把系统讲明白。`

This is not article-style looseness. It means the document must be technical, but it must still be written for Chinese embedded learners who need to understand the system quickly.

Internal reader-clarity standard:

- The final language should feel like an internal engineering handoff written by a strong big-company engineer who can explain the whole design patiently and clearly.
- Keep the visible form serious and professional, but make the reasoning easy to follow for a junior embedded engineer.
- Do not reduce technical depth. Instead, explain the deep mechanism step by step: why the module exists, why the route is split this way, what constraint forced the decision, what happens on failure, and how the result is verified.
- Avoid both extremes: do not write like a公众号 article or course handout, and do not hide behind dense jargon, all-English phrasing, or abstract methodology language.
- A good paragraph should leave the reader able to answer at least one practical question: `为什么这样设计`, `异常怎么处理`, `出问题怎么查`, or `怎么证明它对`.

## Source and Design Baseline

Use public engineering practice, user-provided project evidence, and reasonable engineering assumptions. Do not claim access to internal DJI, Huawei, or other company templates.

When the user's later correction conflicts with earlier raw material, follow the later correction and preserve the conflict as a note only when it matters. Do not average two routes into one architecture. For device-App-cloud material, if older notes mention BLE image chunking but the locked route is `控制走 BLE、图片走 Wi-Fi HTTP、AI 走网关、异常回到 IDLE`, the final main architecture must use Wi-Fi HTTP for image payload and BLE for control/status.

Acceptable framing:

- `参考消费电子硬件产品 NPI / EVT-DVT-PVT 验证逻辑`
- `参考 IPD / ASPICE 中需求、设计、测试追溯思想`
- `正式发布设计基线`
- `正式发布版设计说明书`
- `面向小批量试产验证阶段的工程交付基线`

Avoid:

- `某大厂内部模板`
- `内部泄露资料`
- `已完成量产`
- `工厂就绪`
- `EMC/ESD/热设计已通过`
- `自研 PCB 已量产` unless the user provides proof

## Maturity Language

Maturity must be locked from the latest user instruction. Do not force every project into `小批量试产验证` if the user explicitly asks for a final, external, formal release, or mass-production document.

Use `正式发布设计基线` / `正式发布版设计说明书` when the requested document form is a release document. In that case, the visible software/hardware architecture, interface, recovery, verification, production-test, assembly, BOM, and delivery sections must read as a complete production-grade scheme.

For final/external/formal/mass-production deliverables, never expose missing-source disclaimers in the document body. Avoid visible wording such as:

- `未提供资料`
- `没有资料`
- `当前材料`
- `当前不覆盖`
- `不覆盖范围`
- `证据边界`
- `待补充`
- `不声明`
- `后续闭环`
- `补齐`
- `缺少`
- `不完整`
- `待实测`

When a production-relevant detail is absent from the user's material, choose one of two paths:

1. Fill it as a conservative, production-suitable engineering scheme and write it as the project-adopted design.
2. Remove the topic from the visible body if a responsible scheme cannot be inferred without inventing product-specific facts.

Hardware final-release documents should convert common gaps into adopted schemes, including CAN transceiver model class, terminal matching value, protection devices, power topology, peak-current budget, thermal path, EMC/ESD measures, structure/assembly, production-test fixture contacts, programming/IAP/reset checks, traceability records, and production BOM selection.

Keep proof-only claims out unless the user provides evidence. This includes completed factory run, certification pass, measured EMC/ESD/thermal/current result, field reliability result, and already-produced MP batches. Write design controls, derating limits, acceptance criteria, and production-test methods instead of visible uncertainty statements.

If the user does not specify maturity, default to evidence-bounded `产品化验证` / `小批量试产验证`.

This avoids both weak and inflated framing:

- Do not write the project as a cheap demo, toy prototype, or casual course exercise.
- Do not claim certification, measured results, factory readiness, or MP completion without user evidence.
- For formal release documents, the voice should be serious and release-grade. Avoid phrases that sound like classroom guidance, such as `不要看到...就...`, `看起来都不对`, `主观猜测`, or `为了让你理解`. Use formal engineering wording: `故障定位应按...分层执行`, `该流程用于将端到端异常拆分为可验证环节`, `量产控制项按接口、电源、保护、装配和产测链路分层验收`.

Good wording for final release documents:

- `本设计采用隔离收发、端接匹配与接口保护组合，保证 CAN 诊断链路在整车线束环境下具备稳定通信和抗扰能力。`
- `电源链路按输入保护、降压转换、低噪声供电和负载分区组织，峰值电流按最大发射、显示刷新和接口通信同时工作场景留出裕量。`
- `产测流程覆盖烧录、IAP、复位、CAN 通信、供电电流、接口防呆和序列号写入，批次记录用于追溯硬件版本、固件版本和关键测试结果。`

## Engineering Writing Rules

Write like an engineer explaining a real system:

- Explain why the design exists, not only what was used.
- Tie every major section to implementation, debugging, verification, release controls, or issue disposition.
- Prefer mechanisms, constraints, thresholds, and tradeoffs over adjectives.
- Use concrete failure handling: who detects the fault, who cleans resources, what state the system returns to, what the user sees, and how to verify recovery.
- Use measured data when available. For final/external/formal/mass-production documents, write missing numeric content as design targets, derating limits, acceptance criteria, or production-test thresholds; do not expose `待实测` or similar placeholder wording in the body.
- Use Chinese as the primary language. Keep English only for true technical identifiers, protocol/API names, commands, file names, code symbols, and widely accepted abbreviations.
- For every dense term, make the surrounding explanation human-readable. Example: write `BLE GATT 负责控制命令和状态同步` rather than only `BLE GATT control/status plane`.
- Prefer `讲清楚为什么这样设计、出问题怎么定位、怎么验证` over generic wording such as `提升稳定性` or `构建闭环`.

Avoid AI-flavored or promotional sentences unless they are immediately backed by a concrete mechanism. Weak phrases include:

- `先进架构`
- `高可靠`
- `完整闭环`
- `全面提升`
- `显著增强`
- `智能化能力`
- `一站式`
- `赋能`
- `端到端闭环` without naming the detector, cleanup path, next state, and verification method

Rewrite them as concrete behavior: what component detects the event, what resource is released, what state is entered, what the user sees, and how the result is verified.

## External Document Hygiene

For final/external/formal/mass-production deliverables, the visible document must look like a real production engineering document, not an AI-assisted editing artifact.

Do not include:

- document version-description pages
- revision history, change history, or modification-record tables
- labels such as `可读性版本`, `可读性版`, `AI 优化版`, `润色版`, `V1.3 样式`, or similar process names
- visible statements that the document was generated, optimized, polished, reviewed, or rewritten by AI
- `AI`, `ChatGPT`, `Codex`, `imagegen`, prompts, generation records, figure-source hash tables, `SHA-256`, audit results, or provenance notes unless the term is a real product feature name supplied by the user
- filenames, headers, footers, cover metadata, or package names that expose revision iteration or AI processing

Keep process evidence internal. Audit logs, imagegen manifests, hash checks, prompt notes, and revision notes can be used by the agent while working, but they must not enter the customer-facing DOCX or external delivery package unless the user explicitly requests an internal QA package.

For Chinese embedded engineering delivery, the document should:

- speak plainly without becoming shallow
- explain the engineering mechanism behind each conclusion
- point out real constraints and tradeoffs directly
- avoid fake polish, HR phrasing, marketing phrasing, and vague “methodology” language
- help the reader build project understanding, not just admire the document format

Avoid visible training/course language in final engineering documents unless explicitly requested:

- `学员`
- `面试`
- `快速上手`
- `训练路线`
- `核心概念`
- `教学 demo`
- `项目亮点总结`

Translate those goals into engineering headings:

- `系统责任边界`
- `关键设计取舍`
- `异常恢复与降级策略`
- `调试与问题定位路径`
- `验证项目与验收标准`
- `发布交付与量产控制项`

## TOC and Readability Standard

A weak directory makes the document feel generated even when the body is decent. Build the TOC as an engineering route map, not as a list of generic topics.

Treat the directory/TOC as a first-class deliverable. A document is not final if the body is detailed but the TOC looks coarse, generic, or hastily assembled.

A strong TOC should show:

- system entry before subsystem details
- hardware/software responsibility boundary
- control path and payload path
- runtime/task/data pipeline sections
- protocol/interface sections
- exception recovery and troubleshooting sections
- verification and release-control sections
- figure/table landing points planned near the relevant mechanism

Avoid rough TOCs:

- only H1 chapters with little H2/H3 depth
- generic headings such as `系统设计`, `模块设计`, `测试`, `风险` without mechanism names
- duplicated overview chapters
- training-course titles hidden in the directory
- manufacturing-heavy chapters in validation-only documents; for final/external release documents, convert manufacturing content into adopted production design controls instead of exposing validation limitations
- manual-looking TOC pages without stable dotted leaders, right-aligned page numbers, readable hierarchy, or rendered spacing checks
- polished cover pages that hide weak section naming or missing mechanism coverage

For learner-facing delivery, the TOC should be readable in one pass. A reader should understand the product route, important mechanisms, and document depth from the directory alone.

Use real Word TOC generated from Heading styles whenever possible. Prefer dotted leaders, right-aligned page numbers, and clear level-1/level-2 hierarchy. Choose one-column or two-column layout by rendered readability: a two-column TOC is acceptable when it is clean and compact; a single-column TOC is better when section names wrap, page numbers crowd, or the page looks compressed. It is acceptable for a formal TOC to span multiple pages if readability improves.

Before final handoff, inspect the TOC page itself, not only the heading list. If a user screenshot of the TOC would reasonably look `粗糙`, cramped, generic, or hastily assembled, the document is not ready.

## High-Value Content

Prioritize content that helps the reader answer hard project questions:

- What is the product route and end-to-end user flow?
- Which parts run on device, app, gateway, cloud, and test tools?
- What is control data and what is payload data?
- Why this communication path instead of another?
- How do tasks, callbacks, queues, buffers, and state machines cooperate?
- How are disconnects, timeouts, packet loss, memory pressure, invalid input, and low power handled?
- What design targets, acceptance criteria, and production controls prove the scheme is releasable?

Cut or compress:

- Generic background knowledge
- Long datasheet summaries
- Decorative product/market prose
- Repeated architecture explanations
- Unsupported “reliability improved” claims
- “Looks professional” content that does not help implementation, debugging, verification, or explanation

## Software Depth Standard

Software documents must not be API summaries. They should explain how the system runs.

Cover, when applicable:

- Layering: BSP/Driver/Middleware/Application/Protocol/Debug
- Startup and initialization order
- RTOS task/thread/event-loop model
- Queue, timer, callback, ISR, semaphore/event group, and resource lifetime
- Sensor/camera/audio acquisition pipeline
- Control channel vs payload channel
- Protocol versioning, packet fields, ordering, CRC/integrity, timeout, retry, reconnect, deduplication
- App orchestration, local state, caching, permissions, foreground/background behavior
- Backend/gateway request validation, error code, timeout, fallback, rate limit, privacy/config boundary
- State machine and recovery path
- Logs, metrics, debug commands, smoke/soak tests, CI, release scripts

For payload-heavy systems, explain the tradeoff instead of making a slogan:

- BLE/UART/MQTT can be suitable for control/status.
- Wi-Fi/HTTP/TCP/local upload can be suitable for image/audio/file payloads.
- App/gateway can carry interaction, orchestration, caching, retries, and AI request composition.

## Hardware Depth Standard

Hardware documents must not be component datasheets. They should explain why the board/platform can support the product route.

Cover, when applicable:

- Main controller/SoC/MCU resource fit
- Camera/audio/sensor interface and data path
- PSRAM/storage/memory and its software impact
- Wireless/RF/antenna/interface constraints
- Power tree, operating modes, peak current, low-power constraints, and battery estimation
- USB/debug/programming/bring-up path
- Hardware/software interface: pins, buses, interrupts, reset/status lines, exposed events
- Mechanical/assembly boundary, optical/acoustic/RF placement constraints
- Bring-up checklist, interface validation, test points, failure diagnosis
- BOM substitution, lifecycle, supply, cost, and release supply controls

If the current implementation uses a module such as an ESP32-S3 camera board, handle it by document maturity:

- For validation-only documents, explain the module/platform boundary and what it validates.
- For final/external/formal/mass-production documents, translate the module route into a production-intent hardware scheme: main board responsibility, connector and fixture access, power/protection/RF/thermal/assembly controls, and BOM selection. Do not leave the visible document as a module limitation list.

## Visual Standards

Use visuals to clarify engineering structure, not to decorate.

For this skill's final Word deliverables, custom explanatory figures must use pure `imagegen` outputs when available. The exception is a user-provided authoritative figure, schematic, screenshot, measurement chart, or an explicit user instruction to use another method. Such exceptions must be labeled as source figures or user-approved exceptions, not custom imagegen figures.

Do not replace `imagegen` with locally scripted diagrams for final explanatory figures. Do not redraw or post-process engineering labels, arrows, cropping, resolution, module boxes, icons, colors, or layout. Word-side scaling and external captions are allowed; pixel-level modification is not.

The final inserted custom figures must be the selected imagegen outputs themselves. Do not locally redraw labels, arrows, icons, module boxes, or text and then call the result imagegen. Bad imagegen text, wrong arrows, or poor layout must be solved by regenerating and screening more candidates, shortening labels, moving detail to Word captions/tables, or reporting that the pure-imagegen figure could not be accepted.

For real boards, product appearances, brand marks, chip photos, or service icons, ask the user to upload or identify the real asset before using it. Use such material sparingly to improve clarity. If no real asset is provided, do not invent a specific physical board/product photo.

Before generating final DOCX files, create a figure coverage plan with:

- target section
- purpose
- visual type
- generation method
- caption

Visual style:

- white or very light background
- restrained engineering palette
- deep teal/dark blue-gray for main flow
- light gray for neutral boundaries
- orange only for exception, fallback, or recovery paths
- short Chinese-first technical labels
- clean arrows
- minimal icons
- no image title
- no marketing layout
- no glowing effects
- no dense paragraphs inside images
- few precise module boxes in the main architecture figure; do not turn the figure into a component inventory
- arrows only for the core chain; do not draw every possible internal dependency
- long explanations, dense fields, and edge cases belong in the Word body, sequence diagrams, or tables, not in the main architecture figure

For a device-App-cloud system architecture, a common first-read chain is:

`控制走 BLE -> 图片走 Wi-Fi HTTP -> AI 走网关 -> 异常回到 IDLE`

If the project uses a different route, lock that route explicitly before drawing. Do not mix BLE image chunk transfer and Wi-Fi HTTP image transfer in one final architecture diagram unless the document is explicitly comparing alternatives.

Put the title in the Word caption:

`图 2-1 系统总体架构图`

Do not put large title text inside the image itself.

Figure language rules:

- Default figure labels should be Chinese because the reader is Chinese.
- Preserve English only for actual identifiers: `ESP32-S3`, `BLE GATT`, `Wi-Fi`, `PSRAM`, `FastAPI`, `Qwen-VL`, `CosyVoice`, `CRC`, `MTU`, `Frame ID`, `request_id`, `ADB`, `pytest`.
- Translate explanatory labels: use `眼镜端采集`, `分片发送`, `App 重组`, `AI 网关`, `云端 TTS`, `本地 TTS 回退`, `异常恢复`, `验收脚本`.
- Do not make diagrams English-only to look international. In this document family, that is a readability failure.
- If `imagegen` produces garbled Chinese or wrong English, regenerate with shorter labels first. If still unreliable, use numbered callouts with Word-side explanations, request an authoritative source figure, or report the blocker. Do not use imagegen for visual style reference and correct labels locally.
- Screen every imagegen engineering figure for wrong text, wrong arrows, random modules, large in-image titles, decorative icons, over-coloring, and technology-poster aesthetics. Reject candidates that fail these checks.

Coverage guidance:

- Software detailed design around 25-35 pages usually needs 8-12 meaningful figures.
- Hardware detailed design around 12-18 pages usually needs 5-8 meaningful figures.
- A hardware document with only one hardware block diagram is under-illustrated.
- Counts are not the goal; missing mechanism coverage is the problem.

Typical software figures:

- system end-to-end architecture
- main control/data sequence
- device software layering
- task/event/queue model
- capture-to-transfer data pipeline
- BLE/Wi-Fi/API responsibility split
- protocol packet/framing mechanism
- app-gateway-model architecture
- state machine and exception recovery
- CI/smoke/soak verification flow
- logging and troubleshooting path

Typical hardware figures:

- hardware system block diagram
- main controller and peripheral interface map
- camera/PSRAM/data path
- wireless/RF/antenna constraint diagram
- power tree and operating modes
- USB/debug/bring-up connection map
- mechanical/assembly boundary
- production validation and release-control flow

## Verification and Release Controls

Use measured data if the user provides it. If not, write design targets, acceptance criteria, derating limits, and production-test thresholds. For final/external/formal/mass-production documents, do not write placeholder measurement phrases such as `待实测`, `暂无数据`, or `后续补充`.

Useful design/verification fields:

- connection time, reconnect time, packet loss, control latency
- payload size, transfer throughput, timeout rate
- capture time, image size, frame failure rate
- heap peak, task stack high-water mark, queue depth, CPU load
- app foreground/background recovery
- AI gateway latency, timeout, retry, fallback result
- current draw by mode, battery estimate, thermal observation
- bring-up result, rail voltage, interface signal validation
- smoke/soak test conditions, acceptance criteria, measured result

Verification tables should include:

- test item
- test condition
- method/tool
- expected result
- design target or measured/result value
- pass/fail
- release control or disposition

## Final QA Standard

Before handoff, the documents must support these reader questions:

- What is the product and its main user flow?
- Why is the architecture split this way?
- What does each module own?
- How does data move across device/app/gateway/cloud?
- How does the system recover from common faults?
- What acceptance criteria and production controls prove the release scheme?
- Where are the strongest design tradeoffs?

If the documents cannot answer these, they are not final.

Run a three-pass review before final handoff:

1. Route and truth pass: check maturity wording, production-scheme completeness, route consistency, no visible gap/disclaimer wording, no demo framing, and no unproved certification/factory-pass claims.
2. Reader pass: check Chinese-first readability, mechanism-specific headings, plain engineering explanations, and no HR/training/marketing language in final engineering sections.
3. Visual pass: check figure coverage, imagegen provenance, candidate rejection, restrained visual style, Word captions, no English-only diagrams, and no orange used outside exception/fallback/recovery paths.

For final/external/formal/mass-production deliverables, also extract or inspect the final DOCX text and scan for forbidden gap phrases:

`未提供资料`, `没有资料`, `当前材料`, `当前不覆盖`, `不覆盖范围`, `证据边界`, `待补充`, `不声明`, `后续闭环`, `补齐`, `缺少`, `不完整`, `待实测`, `暂无数据`, `后续补充`

Any hit in the visible document must be rewritten as an adopted production scheme, release control, acceptance criterion, or removed before handoff.

Also scan the final DOCX text, headers, footers, cover metadata, and filenames for process/provenance phrases:

`版本说明`, `版本修订`, `修订记录`, `修订历史`, `变更记录`, `可读性版本`, `可读性版`, `AI`, `人工智能生成`, `ChatGPT`, `Codex`, `imagegen`, `图源 hash`, `SHA-256`, `审计结果`, `生成记录`, `润色`, `优化版本`

Any hit must be removed unless it is a user-supplied real product feature name.
