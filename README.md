# 🛡️ Fraud & Risk Decisioning Platform
**End-to-End Machine Learning System for Financial Loss Mitigation**

## 📌 Business Value
Este proyecto es una solución diseñada para reducir las pérdidas financieras por fraude en transacciones bancarias.
* **Objetivo:** Identificar transacciones de alto riesgo en tiempo real.
* **Impacto:** Optimización basada en una **Matriz de Pérdida Financiera**, reduciendo la pérdida financiera simulada en un 21%.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Model:** XGBoost (entrenado con el dataset de Crédito de Kaggle).
* **API:** FastAPI (Asíncrono para alta concurrencia).
* **Containerization:** Docker.
* **Explainability:** SHAP-based explainability para auditabilidad.
* **Tracking:** MLflow para registro de experimentos.

## 📊 Features
* **Three-way decision engine:** El sistema decide entre: Aprobado / Revisión Manual / Rechazado.
* **Explainability:** Cada decisión incluye una explicación de qué variable (monto, distancia, etc.) influyó más en el veredicto.

## 🚀 Cómo ejecutarlo (Docker)
```bash
docker build -t fraud-system .
docker run -p 8000:8000 fraud-system
