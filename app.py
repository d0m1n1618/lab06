from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI(
    title="ML Prediction API",
    description="Proste API do predykcji z użyciem modelu LinearRegression",
    version="1.0.0"
)

#Dane treningowe i model
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 60, 70, 80, 90])

model = LinearRegression()
model.fit(X, y)


#Model danych wejściowych
class PredictionInput(BaseModel):
    hours: float = Field(..., gt=0, description="Liczba godzin nauki, musi być > 0")

#Własna obsługa błędów walidacji
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Nieprawidłowe dane wejściowe",
            "details": exc.errors(),
            "message": "Sprawdź, czy przesłano wymagane pole 'hours' i czy ma poprawną wartość większą od 0."
        },
    )

#Endpoint główny
@app.get("/")
def home():
    return {"message": "API działa poprawnie"}

#Endpoint health
@app.get("/health")
def health():
    return {"status": "ok"}

#Endpoint info
@app.get("/info")
def info():
    return {
        "model_type": "LinearRegression",
        "number_of_features": 1,
        "feature_names": ["hours"],
        "target_name": "predicted_score",
        "training_samples": len(X)
    }

#Endpoint predykcji
@app.post("/predict")
def predict(data: PredictionInput):
    prediction = model.predict([[data.hours]])[0]
    return {
        "input_hours": data.hours,
        "predicted_score": round(float(prediction), 2)
    }