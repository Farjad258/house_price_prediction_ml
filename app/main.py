from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()
# model = joblib.load("House_Price_Model.pkl")
# Get the absolute path to the model file
model_path = os.path.join(os.path.dirname(__file__), "model", "House_Price_Model.pkl")
model = joblib.load(model_path)

# Define input schema
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict")
def predict(features: HouseFeatures):
    # Convert input to pandas DataFrame
    input_df = pd.DataFrame([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]], columns=[
        "MedInc", "HouseAge", "AveRooms", "AveBedrms",
        "Population", "AveOccup", "Latitude", "Longitude"
    ])
    
    # Predict
    prediction = model.predict(input_df)[0]
    return {"predicted_price": prediction}
