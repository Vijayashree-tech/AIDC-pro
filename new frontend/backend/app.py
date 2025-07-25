from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(_name_)

# Load the trained model
model = joblib.load("water_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract features
    rainfall = data.get("rainfall")
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    soil_type = data.get("soil_type")
    crop_type = data.get("crop_type")
    acres = data.get("acres")

    # Prepare input as a DataFrame
    input_df = pd.DataFrame([{
        "rainfall": rainfall,
        "temperature": temperature,
        "humidity": humidity,
        "soil_type": soil_type,
        "crop_type": crop_type,
        "acres": acres
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]

    return jsonify({"prediction": round(prediction, 2)})

if _name_ == '_main_':
    app.run(debug=True)
