# Parallel Agent Workflow

Use this workflow when subagents or parallel agent tools are available and the task is large enough to benefit from division of labor. If no subagent capability is available, run the same role checklist sequentially in the main agent.

This reference controls coordination only. It does not replace the document standards, output templates, figure rules, DOCX audits, imagegen purity rules, or final handoff gates.

## Control Model

One main controller owns the delivery. Subagents may produce analysis, draft sections, figure plans, source maps, or QA findings, but they must not produce or hand off the final DOCX package.

The controller must:

- lock the engineering boundary before any body drafting starts
- keep the canonical route, maturity, output package, and visual asset policy in one shared brief
- assign narrow work packages with explicit inputs, forbidden actions, and expected output
- merge all subagent work into one consistent software/hardware document set
- run the final route/truth, reader, visual, DOCX, style, and imagegen purity checks

## Serial Stages

Run these stages in the main controller only:

- User alignment gate: confirm product route, technology stack, release maturity, output package, and real visual assets.
- Route lock: resolve conflicting architecture notes before writing body text.
- Document set decision: choose two DOCX files, one combined sample, PDF export, or package.
- Final chapter map approval by the controller: ensure software, hardware, figures, and verification share one route.
- Final DOCX generation: only the controller assembles final Word deliverables.
- Final verification: only the controller claims completion after the required audits and reviews.
- Git or external delivery: only the controller commits, pushes, packages, or reports final files.

Do not ask subagents to resolve high-impact product truth conflicts independently. They must report conflicts back to the controller.

## Parallel Stages

After the route is locked, the controller may run these work packages in parallel:

- Software design: modules, runtime flow, protocol handling, state transitions, exception recovery, source-code mapping when available, and software verification.
- Hardware design: power, interfaces, protection, EMC/ESD, thermal path, structure/assembly, production test, BOM and release controls.
- Figure planning: figure coverage plan, imagegen prompt intent, candidate screening criteria, captions, and imagegen evidence-log inputs.
- Source/evidence mapping: user facts, verified facts, engineering assumptions, files, logs, screenshots, schematics, measurements, and values that must remain design targets.
- QA review: route contradictions, proof-only claims, forbidden external-document phrases, weak TOC depth, under-illustrated sections, and missing audit steps.

The controller should run fewer packages for small tasks. For a narrow revision, parallelize only the relevant slice and QA.

## Work Package Template

Each subagent assignment should include:

- Locked brief: product type, canonical route, technology stack, maturity, reader, output package, and visual asset policy.
- Scope: exact subsystem, document section family, or review surface owned by the subagent.
- Inputs: source files, user notes, existing DOCX files, screenshots, schematics, logs, and relevant references.
- Required references: the specific skill reference files the subagent must read.
- Forbidden actions: no final DOCX generation, no Git operations, no user-facing package creation, no invention of proof-only claims, no route changes without reporting.
- Output format: concise Chinese engineering prose or tables ready for controller integration, plus assumptions, conflicts, missing evidence, and verification notes.
- Handoff: list changed/drafted sections, figures/tables proposed, unresolved decisions, and any text that must not enter external DOCX files.

## Role Contracts

### Controller

Own the final system route, consistency, and deliverable quality. The controller may reuse subagent wording, but must rewrite as needed so the final document reads as one engineering handoff.

### Software Design Agent

Produce software mechanism content after route lock. Cover design goal, constraints, chosen design, failure handling, verification, and reader takeaway. Keep English only for real identifiers.

### Hardware Design Agent

Convert relevant hardware gaps into adopted production-suitable schemes or release controls. Do not claim completed certification, factory readiness, measured results, or MP batches without user evidence.

### Figure Agent

Create a figure coverage proposal and imagegen prompt intent. It may screen candidate figures when instructed, but final selected assets, hashes, insertion, and purity audit remain controller responsibilities.

### Source Mapping Agent

Map source materials to document claims. Separate user-provided facts, verified facts, assumptions, design targets, and unsupported measured-result claims. Keep this as internal evidence unless the user requests an internal QA package.

### QA Agent

Review drafts against route/truth, reader, visual, external-document hygiene, and completion gates. Report findings with section names and concrete fixes. QA findings are internal process evidence and must not be inserted into external DOCX files.

## Merge Rules

The controller must reconcile all parallel outputs before DOCX generation:

- Route conflicts: stop and resolve through controller judgment or user alignment before drafting final text.
- Terminology conflicts: choose one Chinese-first terminology set and apply it across software, hardware, figures, and captions.
- Maturity conflicts: follow the latest user-locked maturity and rewrite gap language into schemes, acceptance criteria, or release controls.
- Figure conflicts: keep figures that explain the route; move dense detail into captions, tables, or body text.
- Evidence conflicts: include measured claims only when supported; otherwise express them as targets, derating limits, acceptance criteria, or omit them.

Subagent drafts are not authoritative. The final DOCX is authoritative only after controller integration and audit.

## Fallback Without Subagents

When subagents are unavailable, do not skip the workflow. Run the same roles sequentially:

1. Controller locks the brief.
2. Draft software content.
3. Draft hardware content.
4. Build the figure plan.
5. Map source/evidence and assumptions.
6. Run QA against the same gates.
7. Generate and audit final DOCX files.

Report that the delivery used sequential fallback only if the user asked how the work was performed. Do not put this process detail in external deliverables.
