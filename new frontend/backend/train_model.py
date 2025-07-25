import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

# Sample dataset (you can replace this with your actual dataset)
data = pd.DataFrame({
    "rainfall": [100, 150, 200, 80],
    "temperature": [30, 32, 28, 35],
    "humidity": [70, 65, 80, 60],
    "soil_type": ["loam", "clay", "sand", "loam"],
    "crop_type": ["rice", "wheat", "maize", "rice"],
    "acres": [2, 1.5, 3, 2.5],
    "water_required": [300, 250, 400, 350]  # target variable
})

X = data.drop("water_required", axis=1)
y = data["water_required"]

# Categorical columns
categorical_features = ["soil_type", "crop_type"]

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'
)

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(pipeline, "water_model.pkl")
print("✅ Model trained and saved as water_model.pkl")
