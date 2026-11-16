---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-05T15:30:00-06:00"
---
# Build Desk Clock

Goal: produce a production Emery PBW from native C and Clay source.
Inputs: `watchface/src/`, pinned npm package, generated numeral masks.
Execution: follow `knowledge/procedural/build_watchface.md`.
Output: `dist/Desk-Clock-0.1.0.pbw`.
Safety: no store publication without explicit instruction; serialize emulator access.
Failure: stop on failing tests, invalid settings, mismatched native output, or fixture leakage.
