from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="House Price Prediction API")

# Load model
model = joblib.load("model/House_Price_Model.pkl")

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}

@app.post("/predict")
def predict(
    MedInc: float,
    HouseAge: float,
    AveRooms: float,
    AveBedrms: float,
    Population: float,
    AveOccup: float,
    Latitude: float,
    Longitude: float
):
    features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                          Population, AveOccup, Latitude, Longitude]])
    
    prediction = model.predict(features)

    return {
        "predicted_house_price": float(prediction[0])
    }
