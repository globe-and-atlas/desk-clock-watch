---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-05T15:30:00-06:00"
---
# Build and QA

1. Run `node watchface/settings.test.js` for actual Clay Save/Cancel/reload coverage.
2. Run `python3 -m pytest tests/ -q` for24×60 clock bounds/time-format coverage, battery boundaries, rounded glyph counter checks.
3. Run `python3 execution/build.py` for clean production build with DESK_* variables removed.
4. Run `python3 execution/verify.py` for PBW identity/platform/native binary matching.
5. After a fixture is installed by the emulator owner, run `python3 execution/capture_native.py --monitor PORT` for22 exact numeral/palette/date/AMPM/battery checks.
6. Native screenshots require explicit ownership of the shared Emery emulator. Use fixture time/battery only in fixture builds.
7. Rebuild production after fixture screenshots. Never copy a fixture PBW to dist.

Fixture build: in watchface, `pebble clean`, then `DESK_FIXTURE=1 pebble build`.

Generated mask source: `python3 execution/generate_digits.py`.
