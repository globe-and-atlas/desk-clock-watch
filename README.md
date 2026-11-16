---
generated_by: "OpenAI Codex (GPT-6; exact variant not exposed)"
timestamp: "2026-11-05T15:30:00-06:00"
---
# Desk Clock

A warm bedside clock for Pebble Time 2. Rounded Fredoka digits sit inside a simple rounded display; a date and centered battery group sit beneath.

- Six preset palettes: Cream & red, Mint, Ice blue, Night cyan, Coffee, Black & white.
- Custom background/clock digits, labels/battery, and display/frame colors.
- Watch-default, 12-hour, or 24-hour time. AM/PM appears above the display in 12-hour mode.
- Optional word, ISO, US, or EU dates.
- Real battery percentage and four charge bars.
- Updates on minute changes and battery/settings events; no continuous animation.

## Build
```sh
npm install --prefix watchface --ignore-scripts
python3 execution/generate_digits.py
node watchface/settings.test.js
python3 -m pytest tests/ -q
python3 execution/build.py
python3 execution/verify.py
```
Production output: `dist/Desk-Clock-0.1.0.pbw`.

## Native QA
Root session owns the shared emulator. Fixture builds use `DESK_FIXTURE=1 pebble build` after `pebble clean`, from `watchface/`. Fixture-only integer AppMessage keys: 11000 hour (0–23), 11001 minute (0–59), 11002 seconds (0–59), 11004 battery (0–100). Date stays Thursday, November 5, 2026. Fixture defaults: 10:08, battery82. Root native suite: `python3 execution/capture_native.py --monitor PORT` after fixture installation; this does not install or boot an emulator.

Never publish a fixture build. `execution/build.py` clean-builds with DESK_* variables removed. Emery, Chalk, and Gabbro are supported.

## License
Fredoka is distributed under SIL Open Font License1.1; see `licenses/Fredoka-OFL.txt`. Original variable font is preserved in `assets/fonts/Fredoka-Variable.ttf`. Numeral masks are generated locally. No font is copied from a clock manufacturer.

## Public release
https://apps.repebble.com/d8d7cbfc9a3f4aaea111e4ca

Version 0.1.0. First gallery image cycles through 6native color palettes; four static previews follow. Public GIF and production PBW verified against local release files.


## Round-compatible release — 0.1.1

Desk Clock includes native layouts for Pebble Time2 (Emery200×228), original Time Round (Chalk180×180), and Round2 (Gabbro260×260). The rectangular layout and existing settings identities are preserved.

Build: `python3 execution/build.py`, then `python3 execution/verify.py`. Local bundle: `dist/Desk-Clock-0.1.1.pbw`. Native round previews: `media/round/`. Repeatable fixture/capture instructions: [round compatibility QA](knowledge/procedural/round_compatibility.md).

This update is [publicly available](https://apps.repebble.com/d8d7cbfc9a3f4aaea111e4ca) with round screenshots. Public PBW bytes and screenshot pixels verify; physical-watch validation remains separate.
