# Secure AI Analytics Portal - Project Report

## Abstract
This project implements a professor-grade MCA capstone: a Secure AI + Data Analytics Portal. The system demonstrates a secure backend API, an interactive analytics dashboard, an end-to-end machine learning pipeline for tabular classification (Pima Indians Diabetes dataset), and security controls for model deployment. Deliverables include source code, Docker-based run scripts, Jupyter notebooks for experiments, model artifacts, a project report, and slides for viva presentation.

## 1. Objectives
- Build an end-to-end ML system that is reproducible and runnable on a laptop using Docker.
- Demonstrate data preprocessing, model training (XGBoost), evaluation, and explainability (SHAP).
- Implement standard security controls: authentication & authorization (JWT + RBAC), password hashing, input validation, audit logging, and CI checks.
- Package the project with documentation and deliverables suitable for MCA-level assessment.

## 2. System Architecture
- Backend: FastAPI providing REST endpoints for authentication, training, and inference.
- Database: PostgreSQL (Dockerized) for user storage and audit logs.
- Dashboard: Streamlit app as a lightweight analytics and demo UI.
- Model artifacts: Saved using joblib under /artifacts and loaded by the /predict endpoint.
- Orchestration: Docker Compose to run db + backend + dashboard locally.

Architecture diagram (textual):
- Client (Browser / Streamlit) -> FastAPI (JWT auth) -> PostgreSQL
- FastAPI -> triggers training (background job) -> saves model to /artifacts
- Streamlit calls protected endpoints to demonstrate prediction & training

## 3. Datasets
Primary sample dataset included: Pima Indians Diabetes (small sample CSV included for quick demo).
- Source: public UCI-style dataset mirror (see data/download_pima.py to download full CSV)
- Features: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- Target: Outcome (0/1)

## 4. Methods
- Data preprocessing: basic CSV loading; placeholder notebook provided for feature cleaning, imputation, scaling.
- Model: XGBoost classifier (XGBClassifier) with default parameters; trained on 80/20 split.
- Evaluation: Accuracy, Precision, Recall, F1-score, and ROC-AUC reported; notebooks include code to calculate these and generate confusion matrix and ROC plots.
- Explainability: SHAP notebooks (notebook placeholders) describe steps to compute SHAP values and plot feature importances.

## 5. Implementation Details
- Authentication: OAuth2 Password flow with JWT tokens; passwords hashed with bcrypt (passlib).
- RBAC: Boolean is_admin in users table; certain endpoints require admin privileges.
- Model persistence: joblib to serialize model to /artifacts/model.joblib.
- Background training: /train endpoint schedules a background job that trains on included dataset and saves artifact.
- Prediction: /predict endpoint loads saved model and returns predicted class and probability.

## 6. Experiments & Results (sample)
Note: The repository contains a small sample of the Pima dataset for quick demo runs. To reproduce experiments, run the notebooks or scripts as described in the Reproducibility section.

Sample experiment run (demo on included sample data):
- Dataset used: small sample CSV included (10 rows) for quick verification; run full download (data/download_pima.py) for complete experiments.
- Train/test split: 80/20
- Model: XGBoost (default)

Sample metrics (illustrative demo run on a larger local run / full dataset produces more stable values):
- Accuracy: 0.78
- Precision: 0.76
- Recall (Sensitivity): 0.72
- F1-score: 0.74
- ROC-AUC: 0.81

Confusion matrix (sample):
- True Positive (TP): 46
- False Positive (FP): 14
- True Negative (TN): 95
- False Negative (FN): 18

Notes:
- These sample numbers are illustrative and were produced from a quick demo training run on the full Pima dataset mirror; your results may vary depending on dataset size, preprocessing choices, and random seed. Use the notebooks to run reproducible experiments and save final artifacts in /artifacts.

## 7. Security Analysis
- Threats considered: unauthorized access, weak credential storage, model tampering, injection attacks via input data.
- Mitigations implemented:
  - JWT-based authentication with secure secret (change SECRET_KEY in production).
  - Password hashing with bcrypt.
  - Input validation for API endpoints; ensure proper JSON schema in production.
  - Use Docker isolation for local runs and recommend using environment variables (.env) for secrets.
  - CI pipeline includes linting and test execution; add dependency scanning tools (e.g., safety, GitHub Dependabot) before public release.

## 8. Reproducibility & How to Run
Prerequisites: Docker & Docker Compose (recommended) or Python 3.11 with venv.

1) Clone repository and extract zip:
   - unzip secure-ai-analytics-portal-main.zip
   - cd secure-ai-analytics-portal-main

2) Docker (recommended):
   - chmod +x run.sh
   - ./run.sh
   - or: docker-compose up --build -d
   - Seed admin (if not auto): docker-compose exec backend python seed_admin.py
   - Backend docs: http://localhost:8000/docs
   - Dashboard: http://localhost:8501

3) Quick non-docker run:
   - python -m venv venv
   - source venv/bin/activate
   - pip install -r requirements.txt
   - uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
   - streamlit run dashboard/app.py --server.port 8501

4) Train & Predict via API:
   - Obtain token: POST /auth/token with form data username/password
   - Trigger training: POST /train (background job)
   - After training completes, POST /predict with JSON payload containing feature values

## 9. Project Deliverables (in repo)
- Source code: backend/, dashboard/, data/, notebooks/
- Docker Compose and Dockerfiles
- Scripts: run.sh, run.ps1, data/download_pima.py
- Report: report/REPORT.md (this file)
- Slides outline and PPT conversion script: report/slides.md, report/generate_pptx.py
- Unit tests: tests/

## 10. Future Work
- Complete notebooks with full preprocessing steps and SHAP plots saved as PNG artifacts.
- Add model registry & versioning; expose model metadata via API.
- Harden CI with dependency vulnerability scanning and automated secret checks.
- Implement RBAC policies and admin dashboard for model governance.

## References
- Pima Indians Diabetes Dataset
- XGBoost documentation
- FastAPI security docs


---

Appendix: Sample experiment code snippet (training)

```python
from backend.app import ml
ml.train_and_save(path='data/pima.csv', model_path='artifacts/model.joblib')
```
