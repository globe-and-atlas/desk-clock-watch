# Errors

Record deterministic errors, root causes, and fixes here.

## 2026-11-05 — Monochrome capture assertion
Battery QA initially selected the outer frame as icon-left when frame and foreground shared black. Restricted the scan to the battery region, then reran all22native cases successfully. Product rendering did not change.

##2026-11-05 — Public PBW storage redirect
Initial public verifier rejected the PBW endpoint redirect because its host allowlist contained only RePebble domains. Observed the public endpoint redirect hostname, allowed the exact store R2host, and verified downloadedPBW SHA256. No signed URL query is logged.
