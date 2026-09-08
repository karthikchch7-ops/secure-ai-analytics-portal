# Slides for presentation (Markdown)

---

# Secure AI Analytics Portal

- Author: MCA Candidate
- Project: Secure AI + Data Analytics Portal

---

# Objectives

- Build an end-to-end ML pipeline
- Demonstrate security controls and reproducibility

---

# Architecture

- FastAPI backend, PostgreSQL DB, Streamlit dashboard, Docker Compose

---

# Dataset

- Pima Indians Diabetes (tabular classification)
- Features: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age

---

# Methods

- Data cleaning, feature engineering
- XGBoost classifier
- Explainability: SHAP

---

# Experiments & Results (sample)

- Train/test split: 80/20
- Sample metrics (demo run):
  - Accuracy: 0.78
  - Precision: 0.76
  - Recall: 0.72
  - F1-score: 0.74
  - ROC-AUC: 0.81

- Confusion matrix (sample): TP=46, FP=14, TN=95, FN=18

---

# Security

- JWT auth, bcrypt passwords
- Input validation, audit logs
- CI tests and dependency scanning recommendations

---

# Demo

- Show dashboard: login, start training, make prediction
- Show notebooks and SHAP plots

---

# Conclusion & Future Work

- Model registry, hardened CI, extended datasets

