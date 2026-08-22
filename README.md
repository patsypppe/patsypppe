# Pranav T Pattanashetty

**Applied machine learning and the infrastructure it runs on.**
M.S. Computer Science at Indiana University Bloomington. Software Development Engineer Intern at SparkFX.

I work on the part of ML that comes after the model trains: making a result reproducible, cheap to run,
and inspectable when it gets something wrong. Most recently that has meant building an evaluation harness
that decides whether an agent change is an improvement or a regression, and can prove the same answer
tomorrow. Before that, three peer-reviewed papers across video classification, biosignal analysis, and
evolutionary optimization of language models, plus a ride-sharing backend built end to end on AWS
managed services with Terraform.

---

## Featured work

### [meridian](https://github.com/patsypppe/meridian) · agent evaluation harness

Answers one question: did this change make the agent better or worse, and can you reproduce that answer
tomorrow. Every trial runs in its own container with its own workdir volume, so nothing leaks between
runs. Scoring uses `pass^k` rather than a single accuracy number, because an agent that passes once in
five attempts is not an agent that passes. A PR gate compares head against the merge base and blocks the
merge only when the drop clears both a tolerance and a significance test.

Python 3.12, Typer, Docker, Postgres with Alembic, Starlette recording proxy, `mypy --strict` and ruff
enforced in CI, 226 unit tests green in under three seconds.

### [ridesharing-app](https://github.com/patsypppe/ridesharing-app) · serverless AWS backend

Six Lambda-backed services (user, driver, ride, payment, notification, websocket) behind an HTTP API
Gateway, with a separate WebSocket API for live location, DynamoDB for state, and Cognito for auth. The
environment is declared in Terraform rather than clicked together in the console. Written as an
infrastructure and architecture study, not a deployed product: the README says exactly which pieces are
built and which are not.

Node.js, Terraform, AWS Lambda, DynamoDB, API Gateway v2, Cognito, CloudFront, EventBridge, SNS.

### [Cricket-Shot-Detection](https://github.com/patsypppe/Cricket-Shot-Detection) · video classification with physics constraints

Classifies cricket batting shots from video across five model variants, including a Vision Transformer,
a 3D ResNet, a CNN-GRU with key-frame selection, and a physics-informed model that adds temporal
continuity, energy conservation, and momentum conservation terms to the classification loss. Grad-CAM is
wired into the prediction path so a call can be inspected frame by frame instead of trusted on an
aggregate. Backs a peer-reviewed publication.

PyTorch, Hugging Face Transformers, OpenCV, Weights & Biases, scikit-learn.

### [Bio-inspired-computing](https://github.com/patsypppe/Bio-inspired-computing) · fine-tuning language models by evolutionary search

Asks how much of a pre-trained model to freeze during fine-tuning by searching for the answer instead of
guessing it. A genetic algorithm and the Whale Optimization Algorithm both search over freezing
percentage and crossover operator for RoBERTa on SST-2. Two findings held across every configuration:
SBX crossover wins, and less freezing wins. Best result 94.67% accuracy. Backs a peer-reviewed
publication.

PyTorch, Hugging Face Transformers and Datasets, genetic algorithms, mixed-precision inference.

### [EMG-Dumbbell-press](https://github.com/patsypppe/EMG-Dumbbell-press) · exercise form from surface EMG

Turns raw two-channel surface EMG into a Good / Fair / Bad form label for a dumbbell press. The useful
signal turned out to be the balance between the deltoid and pectoral channels rather than either alone,
so the pipeline computes per-channel RMS, skewness, kurtosis, and integrated area over sliding windows
and classifies their scaled difference. Best validation accuracy in the committed notebooks is 92.5%, on
a small (~80 sample) split. Backs a peer-reviewed publication.

TensorFlow/Keras, LSTM and recurrent models, pandas, SciPy, scikit-learn.

---

## Research

Three peer-reviewed conference papers, in computer vision, biosignal processing, and LLM optimization.
Each has a public repository above. Citations and DOIs are on my
[LinkedIn](https://www.linkedin.com/in/pranavpattanashetty); email me if you would like the PDFs.

---

## Technologies

**Machine learning** PyTorch · TensorFlow/Keras · Hugging Face Transformers · scikit-learn · OpenCV ·
Weights & Biases · NumPy · pandas · SciPy

**Backend and infrastructure** Python · Node.js · Terraform · Docker · AWS (Lambda, API Gateway,
DynamoDB, Cognito, S3, CloudFront, EventBridge, SNS) · PostgreSQL · Alembic · GitHub Actions · Jenkins

**Frontend** React · TypeScript · Next.js · Tailwind CSS

**Tooling I care about** `mypy --strict` · ruff · pytest · reproducible builds and lockfiles

AWS Certified Cloud Practitioner.

---

## Currently

Building [meridian](https://github.com/patsypppe/meridian), an agent evaluation harness, toward a
release that a team other than mine could adopt. At SparkFX I work on agent-based issue triage in a
Next.js and TypeScript codebase.

Graduating May 2027 and open to new-grad software, machine learning, and cloud engineering roles in the
United States.

---

## Contact

- Email: [ppattana@iu.edu](mailto:ppattana@iu.edu)
- LinkedIn: [pranavpattanashetty](https://www.linkedin.com/in/pranavpattanashetty)
- Bloomington, Indiana
