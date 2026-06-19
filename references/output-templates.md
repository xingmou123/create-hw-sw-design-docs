# Output Templates

## Default Deliverables

For a hardware product with embedded software, default to:

1. `ProductName_软件详细设计说明书_最终交付版_Vx.y.docx`
2. `ProductName_硬件详细设计说明书_最终交付版_Vx.y.docx`
3. Optional `ProductName_最终交付设计文档包_Vx.y.zip`

Use one merged DOCX only for quick samples or when the user asks for a single file.

Do not treat Markdown as final delivery unless the user explicitly asks for draft text only. Markdown can be used internally for outline, figure plan, or content staging.

## Word Requirements

Each final Word document should include:

- cover page with project name, document title, version, date/company/role placeholders when unknown, and evidence boundary
- revision history
- document scope and assumptions
- Word-compatible table of contents based on heading styles
- TOC page inspected after rendering: dotted leaders, right-aligned page numbers, readable spacing, and no cramped two-column layout
- consistent Heading 1/2/3 hierarchy
- explicit Chinese font binding for Word styles and text runs: `ascii`, `hAnsi`, `eastAsia`, and `cs` should resolve to a real Chinese-friendly font such as `Microsoft YaHei` / `微软雅黑`
- no heading paragraph-format flags that show black square markers when Word formatting marks are enabled, especially `keepNext`, `keepLines`, and `pageBreakBefore`
- tables for module responsibility, interfaces, protocols, verification, risks, and delivery list
- figures generated or provided according to the figure plan
- figure captions in body text; no large figure title inside images
- footer with document name, version, and page number when feasible
- versioned filename

Before claiming completion:

- open or inspect the DOCX
- run `scripts/audit_docx.py`
- run a DOCX style audit for heading black-square markers, missing `eastAsia` font binding, and theme font fallback
- verify headings, tables, media, drawing nodes, captions, and image count
- check for obvious blank pages, table overflow, image misplacement, placeholder text, and stale route contradictions

## Chapter Map Quality Gate

Before writing the DOCX body, produce a chapter map with these columns:

| Section | Purpose | Key subsections | Tables | Figures | Evidence boundary |
|---|---|---|---|---|---|

Reject and rewrite the map if:

- most sections have no H2/H3 plan
- sections are broad but do not name the mechanism being explained
- software and hardware maps disagree on the product route
- a visual-heavy section has no planned figure
- verification appears only as a closing formality instead of a real acceptance matrix
- risk sections contain generic risk words without specific closure items

Good section names are mechanism-specific:

- `BLE 控制链路与 GATT 服务设计`
- `Wi-Fi HTTP 图像数据面设计`
- `摄像头采集、PSRAM 缓冲与帧生命周期`
- `状态机与异常恢复路径`
- `电源树、工作模式与峰值电流约束`

Weak section names are too generic:

- `通信模块`
- `图像模块`
- `系统测试`
- `风险分析`

## Figure Coverage Plan Template

Create this before final generation:

| Figure | Target section | Purpose | Visual type | Generation | Caption |
|---|---|---|---|---|---|
| 图 2-1 | 系统总体设计 | Explain device-app-gateway-cloud boundary | Architecture diagram | imagegen | 图 2-1 系统总体架构图 |
| 图 5-1 | 通信协议设计 | Show control channel vs payload channel | Data/control flow | imagegen | 图 5-1 控制链路与数据链路划分图 |

## Imagegen Evidence Log Template

Create this while generating and screening figures. Include it in the handoff summary or package notes for serious deliveries.

| Figure | Prompt file/summary | Candidate count | Selected imagegen output | Final inserted asset | SHA-256 match | Rejected reasons | Allowed operation |
|---|---|---:|---|---|---|---|---|
| 图 2-1 | white background, no title, core route only | 3 | `$CODEX_HOME/generated_images/.../fig_2_1.png` | `assets/figures/fig_2_1.png` | yes | candidate 1: wrong arrows; candidate 2: long title | copy only |

Rules:

- A figure is not accepted just because `imagegen` produced it.
- Reject candidates with wrong route, bad Chinese text, invented labels, marketing style, excessive modules, decorative icons, or orange used for non-exception paths.
- Local correction is not allowed for custom explanatory figures. If a candidate needs text, arrow, module, crop, color, or layout correction, reject it and regenerate.
- The final inserted file must have the same SHA-256 as the selected imagegen output, or be a documented lossless file copy with the same bytes. Do not use locally redrawn or post-processed files.
- Keep the rejected reasons short but concrete enough that another reviewer can see the screening happened.

## Imagegen Purity Manifest

Create a machine-readable manifest beside the DOCX files, for example `imagegen_purity_manifest.json`:

```json
{
  "figures": [
    {
      "figure": "图 2-1",
      "kind": "custom_imagegen",
      "selected_imagegen_output": "E:/Cache/user-32787/.codex/generated_images/.../fig_2_1.png",
      "final_asset": "D:/project/assets/figures/fig_2_1.png",
      "allowed_operation": "copy only"
    }
  ]
}
```

Then run:

```bash
python scripts/audit_imagegen_purity.py --manifest imagegen_purity_manifest.json final-software.docx final-hardware.docx
```

The audit must pass before the delivery is called pure imagegen. It fails when a final asset differs from the selected imagegen output or when the final asset bytes are not present in the DOCX media inventory.

Final figure rules:

- All custom explanatory figures must use `imagegen` when available.
- Do not substitute local script diagrams, SVG/Mermaid/PIL/canvas drawings, screenshots of local diagrams, or post-processed redraws for `imagegen`.
- Do not correct imagegen labels, arrows, icons, module boxes, cropping, colors, or layout locally. Word-side scaling and captions outside the image are allowed because they do not change the image pixels.
- If pure imagegen cannot produce an acceptable figure after reasonable regeneration, state the blocker and leave the figure out or ask the user for an approved exception. Do not silently switch to local reconstruction.
- If the user asked to improve, unify, add, or replace figures, verify that new/changed image files were created and inserted into the DOCX. Do not claim figure optimization from text edits alone.
- Use the same visual language across both documents.
- Keep labels short. Move long explanation to body text.
- Do not put a large title inside the image.
- Insert every planned figure into the DOCX and verify it is present.
- If a figure is skipped, state why and what replaced it.

## Imagegen Prompt Pattern

Use prompts with strong constraints:

```text
Create a clean engineering architecture diagram for a professional hardware/software design document.
White background, restrained big-company engineering style, thin lines, consistent spacing, no marketing composition.
Use dark teal for the main path, white or very light gray for subsystem boundaries, and orange only for exception/fallback/recovery paths.
No large title inside the image. No decorative icons. No glowing effects. No long paragraphs.
Keep modules few and precise. Do not make a component inventory. Use arrows only for the core chain.
Use Chinese-first short technical labels. Keep only true identifiers in English: ESP32-S3, BLE GATT, PSRAM, FastAPI, Qwen-VL, CRC, MTU, request_id.
Show the core route clearly: 控制走 BLE, 图片走 Wi-Fi HTTP, AI 走网关, 异常回到 IDLE.
Final image should look like a readable engineering handoff diagram for Chinese embedded learners, not an AI poster.
```

When Chinese text may be rendered poorly, shorten the Chinese labels, use numbered callouts with Word-side captions/tables, or regenerate. If text is still wrong, reject the candidate. Do not use imagegen only as a style reference and then correct labels locally.

Reject imagegen candidates if they contain garbled or invented text, wrong arrows, wrong route, too many module boxes, a large in-image title, decorative icons, glowing effects, too many colors, or long sentences inside boxes.

Recommended label pattern:

| Concept | Preferred figure label | Avoid |
|---|---|---|
| glasses capture node | `眼镜端采集\nESP32-S3` | `ESP32-S3 Glasses` as the only label |
| control channel | `BLE 控制 / 状态` | `Control Plane` only |
| Wi-Fi image payload | `Wi-Fi HTTP 图像` | `Image Payload` only |
| BLE image chunking, only when it is the locked payload route | `BLE GATT 分片发送` | using BLE chunking labels when the locked route is Wi-Fi HTTP |
| app image handling | `App 取图 / 展示` | `Frame Reassembly` only when the route is not BLE chunking |
| gateway | `AI 网关\nFastAPI` | `FastAPI AI Gateway` only |
| fallback | `本地 TTS 回退` | `Fallback / Error Path` only |
| verification | `本地 CI 验收` | `Local CI Smoke Soak` only |

## Recommended Software Document

Target length for rich learner-facing delivery: normally 25-35 pages when the project has device/app/backend/cloud/test scope. Do not pad; expand only mechanisms that matter.

Use this structure as a starting point:

1. `文档概述`
   - purpose, reader, scope, evidence boundary, assumptions, version
   - current maturity: use the user's locked status; use formal release wording such as `正式发布设计基线` when requested, otherwise use evidence-bounded validation wording

2. `系统总体设计`
   - product function and end-to-end user flow
   - device/app/gateway/cloud/test tool participants
   - software/hardware responsibility boundary
   - figure: system architecture

3. `设备端软件架构`
   - BSP/Driver/Middleware/Application/Protocol/Debug layers
   - module responsibility table
   - control path vs data path
   - figure: device software layering

4. `系统启动与初始化流程`
   - boot sequence, board initialization, peripheral initialization
   - task creation and failure handling
   - initialization timeout/retry/degraded mode

5. `运行时任务与事件模型`
   - RTOS tasks/threads/event loops
   - queues, timers, callbacks, semaphores, event groups
   - stack/heap considerations and scheduling tradeoffs
   - figure: task/event/queue flow

6. `采集与数据通路设计`
   - camera/sensor/audio acquisition
   - frame buffer, PSRAM, compression, chunking, cache, lifecycle
   - memory pressure and invalid-frame handling
   - figure: capture-to-transfer pipeline

7. `通信协议与链路设计`
   - BLE/Wi-Fi/UART/SPI/I2C/CAN/MQTT/HTTP as applicable
   - service/characteristic/API/packet fields
   - versioning, ordering, CRC/integrity, timeout, retry, reconnect, fallback
   - explain why each channel carries control or payload
   - figures: protocol service tree, packet/framing, control vs payload split

8. `App 端交互与本地状态设计`
   - scan/connect/bind/subscription
   - data reassembly, local display, cache/history, permission handling
   - foreground/background recovery and user-visible state

9. `AI 网关与云端能力封装`
   - API routes, request validation, structured response
   - vision/OCR/QA/TTS or model capabilities
   - request_id, error code, timeout, rate limit, fallback, config/privacy boundary
   - figure: app-gateway-model request lifecycle

10. `状态机与异常恢复`
   - device/app/gateway states
   - disconnect, timeout, invalid frame, upload failure, model failure, TTS failure, low power
   - who detects, who cleans, next state, user-visible result, verification
   - figure: state machine and recovery path

11. `内存、性能、功耗与资源约束`
   - heap/stack/buffer budget
   - latency/throughput/packet loss targets or measurements
   - power-sensitive flows and degradation strategy

12. `日志、调试与问题定位`
   - log levels, log points, error codes, metrics
   - serial/ADB/backend logs/test scripts
   - troubleshooting path for common failures
   - figure: log and diagnosis path

13. `测试验证与验收标准`
   - test matrix with condition/method/expected/measured/result
   - smoke/soak, real device, CI, script-based gates
   - figure: verification flow

14. `关键设计取舍与遗留风险`
   - why this architecture/channel/module split
   - rejected alternatives
   - current unresolved risks and next validation items

15. `版本发布与交付清单`
   - version scope, artifacts, configuration, scripts, known issues

16. `附录`
   - protocol tables, API schema, configuration keys, glossary, commands

## Recommended Hardware Document

Target length for rich learner-facing delivery: normally 12-18 pages when the project has MCU/module, camera/sensor, wireless, power, assembly, and bring-up scope.

Use this structure as a starting point:

1. `文档概述`
   - purpose, scope, evidence boundary, assumptions, current maturity

2. `硬件系统总体设计`
   - hardware role in the product
   - module/board/platform boundary
   - major components and responsibility table
   - figure: hardware system block diagram

3. `主控与资源分析`
   - controller/SoC/MCU selection rationale
   - memory, IO, camera/audio/network capability
   - boot, reset, clock, debug, programming
   - figure: controller peripheral/interface map

4. `摄像头、传感器与外设设计`
   - interface, data direction, timing, electrical/placement constraints
   - optical/acoustic/mechanical constraints if applicable
   - figure: sensor/camera data path

5. `存储、PSRAM 与数据缓冲资源`
   - memory role in capture/audio/network workloads
   - buffer size, peak use, failure behavior, software impact

6. `无线链路、接口与天线约束`
   - BLE/Wi-Fi/RF/interface path
   - antenna keep-out, enclosure impact, ESD, connector/test point
   - figure: wireless/RF/interface constraint map

7. `电源与电池管理设计`
   - power tree, rail voltage/current, operating modes
   - peak current, battery estimate, charging/protection if applicable
   - low-power and brownout considerations
   - figure: power tree and operating modes

8. `USB、调试、烧录与产测接口`
   - debug/programming path, serial logs, ADB/USB if applicable
   - test points, fixture considerations, bring-up access
   - figure: debug/bring-up connection map

9. `硬件/软件接口定义`
   - pin map, bus map, interrupts, reset/status lines
   - hardware events exposed to firmware
   - startup/status detection responsibility

10. `结构装配与生产导入边界`
   - enclosure/connector/camera/antenna/battery constraints
   - current module/release-sample boundary vs production-intent hardware
   - figure: mechanical/assembly boundary

11. `硬件 Bring-up 流程`
   - pre-power short check, rail validation, boot/download, peripheral bring-up
   - common faults and diagnosis path

12. `硬件测试与验收标准`
   - power, interface, camera/audio/sensor, wireless, long-run, assembly checks
   - figure: hardware validation flow

13. `BOM、替代料与供应风险`
   - key parts, alternatives, lifecycle, cost, supply constraints

14. `关键设计取舍与遗留风险`
   - why this controller/module/power/wireless/assembly path
   - future production hardware closure items

15. `交付清单`
   - hardware docs, firmware/app/backend versions, test records, known gaps

For formal release-style deliverables, avoid writing body text like a course note. Use `故障定位流程`, `日志字段`, `定位证据`, `不覆盖范围`, `生产导入约束`, and `后续闭环项` instead of casual phrases such as `排障要`, `不要看到`, `看起来都不对`, or `主观猜测`.

## Required Tables

Use tables for dense engineering content:

- module responsibility table
- hardware/software boundary table
- optional source/module mapping table when source code is available and requested
- interface/pin/bus table
- protocol field table
- API request/response table
- state transition table
- exception handling table
- verification matrix
- risk and residual issue table
- release/delivery checklist

## Section Writing Pattern

For every important mechanism, use this compact internal structure:

1. `设计目标`: what problem the section solves.
2. `约束条件`: bandwidth, memory, power, latency, mechanical, cost, or evidence boundary.
3. `方案设计`: exact modules, interfaces, states, data structures, or responsibilities.
4. `设计取舍`: why this design over alternatives.
5. `异常处理`: timeout, retry, fallback, invalid input, degraded mode, recovery state.
6. `验证方式`: how to prove it works; include measured data if available.
7. `工程结论`: one concrete takeaway, not a motivational or interview sentence.

## Final Handoff Template

Report concisely:

- final `.docx` file paths
- optional package path
- checks run
- page count if available
- image/media count and caption count
- figure inventory
- imagegen evidence log summary, selected output hashes, final inserted asset hashes, and `audit_imagegen_purity.py` result
- remaining assumptions/residual risks

Never say final delivery is complete if only an outline, Markdown draft, or unverified document exists.
