from fastapi import FastAPI
import uvicorn
import pandas as pd
import xgboost as xgb
import shap
from pydantic import BaseModel

app = FastAPI(title="Fraud & Risk Decisioning Platform")

# Simulación de entrenamiento (Carga de datos de Kaggle simplificada)
data = pd.DataFrame({
    'amount': [10, 20, 3000, 15, 5000, 25, 4500, 12, 100, 6000],
    'dist_from_home': [1, 2, 500, 1, 900, 3, 700, 2, 10, 1200],
    'is_fraud': [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
})

X = data[['amount', 'dist_from_home']]
y = data['is_fraud']

model = xgb.XGBClassifier()
model.fit(X, y)

explainer = shap.TreeExplainer(model)

class Transaction(BaseModel):
    amount: float
    dist_from_home: float

@app.post("/predict")
async def predict_fraud(transaction: Transaction):
    input_data = pd.DataFrame([transaction.dict()])
    prediction = int(model.predict(input_data)[0])
    probability = float(model.predict_proba(input_data)[0][1])
    
    # Lógica de SHAP para explicabilidad
    shap_values = explainer.shap_values(input_data)
    feature_names = ['Monto de la compra', 'Distancia desde casa']
    main_reason_idx = shap_values[0].argmax() 
    reason = feature_names[main_reason_idx]

    # Motor de decisión de tres vías (Approve / Manual Review / Reject)
    if probability > 0.8:
        status = "REJECTED (Fraud)"
    elif probability > 0.5:
        status = "MANUAL REVIEW"
    else:
        status = "APPROVED"

    return {
        "decision": status,
        "probability": f"{probability:.2%}",
        "explanation": f"Mayor factor de riesgo: {reason}" if status != "APPROVED" else "Comportamiento normal"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
