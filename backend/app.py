from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('../model-training/linear_regression_model.pkl')

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

    # One-hot encode input and align with training columns
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=joblib.load('../model-training/model_columns.pkl'), fill_value=0)

    # Predict
    prediction = model.predict(input_encoded)[0]
    print(f"✅ Predicted water_required: {prediction}")

    return jsonify({"status_code": 200, "prediction_lr": round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)
