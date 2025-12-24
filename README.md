# 🏠 House Price Prediction

*A full-stack AI project to predict house prices using Python, FastAPI, and a trained machine learning model.*  

Predicting house prices helps buyers, sellers, and real estate professionals make data-driven decisions. This project demonstrates a complete workflow: model training, API creation, and cloud deployment using Render.

---

## *🚀 Project Overview*
This project predicts house prices based on key features including:
- Median Income (MedInc)
- House Age (HouseAge)
- Average Rooms (AveRooms)
- Average Bedrooms (AveBedrms)
- Population (Population)
- Average Occupancy (AveOccup)
- Latitude & Longitude  

The workflow is beginner-friendly but fully deployable, demonstrating *end-to-end AI project skills*:
1. Data preprocessing
2. Model training & saving
3. Building a REST API with FastAPI
4. Deploying on Render

---

## *💡 Problem Statement*
Real estate markets fluctuate, and understanding house pricing trends is crucial.  
This project addresses:
- Estimating house prices based on important features
- Building a fully functional API to serve predictions
- Demonstrating cloud deployment and production readiness

---

## *🛠 Tech Stack*
- *Programming Language:* Python 3.x  
- *Libraries:* scikit-learn, pandas, joblib, FastAPI, Pydantic  
- *Deployment:* Render  
- *Version Control:* GitHub  

---

## *📂 Repository Structure*
house-price-prediction/
├─ main.py               # FastAPI application
├─ requirements.txt      # Python dependencies
├─ model/
│   └─ House_Price_Model.pkl  # Trained ML model
└─ README.md             # Project documentation

---

## *⚙ How It Works*
1. *Load the Model*  
   The trained model is stored in model/House_Price_Model.pkl and loaded automatically by main.py.

2. *Input Features*  
   Users provide house details through the /predict API endpoint.  
   Example JSON input:
```json
{
  "MedInc": 8.3,
  "HouseAge": 12,
  "AveRooms": 5.0,
  "AveBedrms": 1.0,
  "Population": 1000,
  "AveOccup": 3.5,
  "Latitude": 34.0,
  "Longitude": -118.0
}

3. *Prediction*
   The API returns the predicted house price in JSON format:
 {
  "predicted_price": 450000.0
 }

🌐 Live Deployment

The project is deployed on Render, making it accessible online:

🔗 https://house-price-prediction-ml-cpip.onrender.com/docs

Use the Swagger UI to interact with the /predict endpoint.

---

## *How to Run Locally*
1. *Clone the repository*
   git clone (https://github.com/Farjad258/house_price_prediction_ml.git)
   cd house-price-prediction

2. *Install Dependencies*
    pip install -r requirements.txt

3. *Run the Prediction Script*
    python main.py

4. *Enter house features and get the predicted price*

---

## *Key Learnings*
1. End-to-end ML workflow: data → model → API → deployment
2. Model saving/loading using joblib
3. Building REST API with FastAPI & Pydantic for input validation
4. Deploying Python applications on cloud platforms (Render)
5. Handling deployment path issues and debugging in production

---

📌 Future Improvements
	•	Add front-end interface for non-technical users
	•	Integrate authentication for API
	•	Expand dataset for more accurate predictions
	•	Enable batch predictions and logging

---

⚡ Why This Project Stands Out
	•	Fully functional production-ready API
	•	Clear documentation and repo organization
	•	Demonstrates problem-solving, ML, API, and deployment skills
	•	Shows readiness for real-world AI/ML projects


    
