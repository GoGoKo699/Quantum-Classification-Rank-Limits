# Hosted mathematics checks

The read-only GitHub Actions workflow compares every mathematical expression on the committed Markdown pages with its actual GitHub rendering at widths 1440 and 760. It records pinned source hashes, MathML structure, screenshots and a revision-bound report. A separate visual review remains necessary.

The collector and checker are an unchanged matched implementation from the research tooling. Node dependencies are pinned in the lockfile. Run from the repository root after installing them with `npm ci --prefix verification/hosted --ignore-scripts` and installing the Playwright Chromium browser:

```sh
node verification/hosted/probe_hosted_math.cjs --root . --repository GoGoKo699/Quantum-Classification-Rank-Limits --revision FULL_COMMIT_SHA --page README.md --output /absolute/new-empty-probe-directory
node verification/hosted/capture_hosted_math.cjs --root . --repository GoGoKo699/Quantum-Classification-Rank-Limits --revision FULL_COMMIT_SHA --contract verification/hosted/math-contract.json --output /absolute/new-empty-capture-directory
```

Replace the revision and output paths with actual values. The representative probe is diagnostic only. The full capture includes all tracked Markdown pages and uses a fresh unsigned-in browser on the public repository. Local source compilation and a passing script do not establish scientific correctness or replace inspecting the actual screenshots.
