# fraud-detection-platform
End-to-end Fraud Detection System using XGBoost, FastAPI, and Docker. Optimized for financial loss mitigation with SHAP-based explainability.

🛡️ Fraud & Risk Decisioning Platform
End-to-End Machine Learning System for Financial Loss Mitigation

📌 Business Value
Este proyecto no es solo un modelo de ML; es una solución de negocio diseñada para reducir las pérdidas financieras por transacciones fraudulentas.

Objetivo: Identificar transacciones de alto riesgo en tiempo real.

Impacto: Optimización basada en una Matriz de Pérdida Financiera, priorizando la reducción de Falsos Negativos (fraudes no detectados) que son los más costosos para el banco.

🛠️ Tech Stack
Language: Python 3.10

Model: XGBoost / Random Forest (entrenado con el dataset de Crédito de Kaggle)

API: FastAPI (Asíncrono para alta concurrencia)

Containerization: Docker

Explainability: SHAP (Para explicar por qué una transacción fue marcada como fraude)

Tracking: MLflow (Para registro de experimentos y métricas)

📊 Dataset Analysis
Se utilizó el dataset de Credit Card Fraud Detection de Kaggle.

Reto técnico: Datos altamente desbalanceados (menos del 1% de fraude).

Solución: Implementación de técnicas de remuestreo y ajuste de umbrales dinámicos para maximizar el ROI.

🚀 Cómo ejecutarlo (Docker)
Para levantar el sistema completo en cualquier máquina:

Bash
docker build -t fraud-system .
docker run -p 8000:8000 fraud-system
Luego, abre http://localhost:8000/docs para probar el sistema en vivo.
