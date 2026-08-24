<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/terminal-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/terminal-light.svg">
  <img alt="Pranav T Pattanashetty. Applied machine learning, and the infrastructure it runs on. M.S. Computer Science at Indiana University, May 2027. SDE Intern at SparkFX working on agent orchestration in TypeScript. Three peer-reviewed papers across vision, biosignals, and LLM tuning. Based in Bloomington, Indiana. Stack: PyTorch, TensorFlow, Hugging Face, scikit-learn, OpenCV, Go, Python, TypeScript, Envoy, JSON-RPC, OpenTelemetry, AWS Lambda, API Gateway, DynamoDB, Terraform, Docker, PostgreSQL, Alembic, pandas, NumPy, SQL, mypy strict, ruff, golangci-lint, pytest, go test -race. Featured repositories: sentinel, meridian, serverless-rideshare-aws, cricket-shot-classification, metaheuristic-llm-finetuning, EMG-Dumbbell-press." src="assets/terminal-light.svg">
</picture>

## Featured work

**[sentinel](https://github.com/patsypppe/sentinel)** · MCP conformance, and a server worth grading

On 28 July 2026 the Model Context Protocol removed sessions and the `initialize` handshake, made
`server/discover` mandatory, replaced server-initiated requests with Multi Round-Trip Requests, and put
Roots, Sampling, Logging, HTTP+SSE and OAuth Dynamic Client Registration on a twelve-month removal clock.
Every server written before that date is now non-conformant in ways its authors have not enumerated.
Sentinel is two halves: a Go broker built natively on the new revision, and a Python harness that scans
any MCP endpoint, grades it rule by rule with a specification citation attached to each finding, and
inventories the deprecated features still in use with the date each becomes removable.

The interesting part is what it refuses to say. Five of the normative MUST requirements cannot be settled
from outside a server — whether a token's audience is really checked, whether an inbound token is
forwarded to a downstream dependency, whether a retried request is idempotent at the *effect* rather than
in the reply. The harness reports those as `INDETERMINATE`, excludes them from the gate, and reprints them
on every scan. A scanner that graded them as passes would be lying, and the clean report it produced would
be worse than no report. The broker implements all five and proves it with tests that have the access a
scan does not — which is why both halves ship in one repository, and why the harness never imports server
internals.

A rule ID also never changes meaning. Three rules turned out to demand more than the specification does;
rather than being redefined in place — which would silently rewrite every report that had already cited
them — they were deprecated and republished under new IDs, with the old ones still evaluable behind a
flag so an earlier report can be reproduced and diffed.

`Go` `Python` `Envoy` `PostgreSQL` `OpenTelemetry` `SARIF` — 13k lines of Go and 5.7k of Python across 36
test files, `golangci-lint`, `go test -race`, `mypy` and `ruff` enforced in CI, and no model API key
required anywhere, which is why the suite is fast and never flaky for a reason outside the repository.

**[meridian](https://github.com/patsypppe/meridian)** · agent evaluation harness

Answers one question: did this change make the agent better or worse, and can you reproduce that answer
tomorrow. Every trial runs in its own container with its own workdir volume, and the suite ships a
contamination probe with a deliberate failing direction — isolation is asserted rather than assumed,
because a probe that cannot fail proves nothing. Scoring uses `pass^k` rather than a single accuracy
number. A PR gate compares head against the merge base and blocks only when the drop clears both a
tolerance and a paired significance test.

Two things it does that the tools it sits beside do not:

*It never trusts the container.* Assertions run on state extracted to the host, after the container is
gone. In 2026 researchers broke several major agent benchmarks through exactly that hole — agents writing
a `conftest.py` that rewrote every test result to `passed`, or replacing `/usr/bin/curl` to emit fake
output. The same rule now applies to Meridian's own task files, since in a CI gate a pull request
*is* the untrusted input: a security pass found a path traversal that could read a host file and print it
into a public PR comment, and closed it along with four smaller siblings.

*It reports its own blind spot.* Every verdict carries the minimum detectable effect — "this run could
only have caught a drop of 0.183 or larger; resolving your 0.030 tolerance would take about 262 tasks."
A PASS from an underpowered suite is not evidence that nothing broke, and a gate that reports those
identically teaches people to trust it exactly when it is least reliable.

It is also measured by itself, and publishes the result including the miss: 0/30 false regressions,
4/5 seeded regressions caught, 5/5 replay fidelity. The one it misses is explained with the arithmetic
rather than tuned away.

`Python 3.12+` `Typer` `Docker` `Postgres + Alembic` `Starlette` `numpy` — `mypy --strict` and `ruff`
enforced in CI, 331 tests across unit, Docker-backed integration, and end-to-end layers.

**[serverless-rideshare-aws](https://github.com/patsypppe/serverless-rideshare-aws)** · serverless AWS backend

Six Lambda-backed services behind an HTTP API Gateway, a separate WebSocket API for live location,
DynamoDB for state, Cognito for auth, and the environment declared in Terraform rather than clicked
together in a console. Written as an infrastructure study, and the README says plainly which pieces are
built and which are not.

`Node.js` `Terraform` `Lambda` `DynamoDB` `API Gateway v2` `Cognito` `EventBridge`

**[cricket-shot-classification](https://github.com/patsypppe/cricket-shot-classification)** · video classification with physics constraints

Five model variants over the same seven-class problem, written to be compared: a CNN-GRU with key-frame
selection, a MobileNet baseline, a 3D ResNet with Vision Transformer, and a physics-informed model that
adds temporal continuity, energy, and momentum terms to the classification loss. A bat swing is a smooth
trajectory, so a model whose per-frame beliefs jump around is wrong even when its final answer is right.

`PyTorch` `ViT` `3D ResNet` `Grad-CAM` `Weights & Biases`

**[metaheuristic-llm-finetuning](https://github.com/patsypppe/metaheuristic-llm-finetuning)** · fine-tuning by evolutionary search

How much of a pre-trained model should you freeze? Usually a guess. This searches for the answer instead:
a genetic algorithm and the Whale Optimization Algorithm over freezing percentage and crossover operator
for RoBERTa on SST-2. Two findings held across every configuration: SBX crossover wins, and less freezing
wins. Best result 94.67% accuracy.

`PyTorch` `Hugging Face` `RoBERTa` `genetic algorithms` `SST-2`

**[EMG-Dumbbell-press](https://github.com/patsypppe/EMG-Dumbbell-press)** · exercise form from surface EMG

A signal problem before it is a modelling problem. Neither the deltoid nor the pectoral channel says much
alone, so the pipeline computes windowed RMS, integrated area, skewness and kurtosis per channel and
classifies the balance between them.

Re-reading it recently turned up target leakage: the label is a threshold on a quantity that is also one
of the model's input columns, so a three-line rule reproduces every label exactly and the accuracies in
the notebooks measure nothing about EMG. The README now leads with that instead of the number, and says
what would be needed to make the question answerable — labels from outside the signal, and a split that
does not put 97%-overlapping windows on both sides. Left up rather than quietly corrected, because the
paper is published and the reasoning is more useful than the figure was.

`TensorFlow/Keras` `LSTM` `SciPy` `pandas`

## Research

Three peer-reviewed conference papers, in computer vision, biosignal processing, and LLM optimization.
Each has a public repository above. Citations and DOIs are on
[LinkedIn](https://www.linkedin.com/in/pranavpattanashetty), or email me for the PDFs.

## Currently

Building [sentinel](https://github.com/patsypppe/sentinel) out from its MVP tier — the parts deliberately
left out are named in its scope section, and the next ones in are consent-registry authorization and
`subscriptions/listen`. Alongside it, taking [meridian](https://github.com/patsypppe/meridian) toward a
release a team other than mine could adopt, and reading the 2026 literature on eval variance closely
enough to argue with it. At SparkFX, agent-based issue triage in a Next.js and TypeScript codebase.

The longer version of all of this, with architecture diagrams, is at
[patsypppe.github.io](https://patsypppe.github.io) — Astro and TypeScript, no client-side JavaScript,
type-checked in CI before it can deploy.

Graduating May 2027, open to new-grad software, machine learning, and cloud engineering roles in the US.

## Contact

[patsypppe.github.io](https://patsypppe.github.io) · [ppattana@iu.edu](mailto:ppattana@iu.edu) · [LinkedIn](https://www.linkedin.com/in/pranavpattanashetty) · Bloomington, Indiana

<sub>The panel above is a static SVG generated by <a href="assets/gen.py"><code>assets/gen.py</code></a>.
No stats service, no API token, no scheduled job, nothing that can decay into "no activity tracked".
Regenerate with <code>python3 assets/gen.py</code>.</sub>
