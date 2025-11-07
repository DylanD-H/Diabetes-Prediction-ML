import pickle
from fastapi import FastAPI
import uvicorn

with open('RandomForestClassifier.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI(title="Diabetes Prediction")


@app.post("/predict")
def predict(patient: dict):
    X = dv.transform([patient])
    y_pred = model.predict_proba(X)[0, 1]
    return{"probability":float(y_pred)}

if __name__ == "__main__":
    uvicorn.run("predict:app", host='0.0.0.0', port=9696)