# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, r2_score
# import joblib

# # Load dataset
# df = pd.read_csv('water_data.csv')  # Ensure the file is in the current directory
# print(df.head())  # Preview data

# # Split into features and target
# y = df['water_required']
# x = df.drop('water_required', axis=1)



# # Train-test split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

# # -------------------------------
# # Linear Regression Model
# # -------------------------------
# lr = LinearRegression()
# lr.fit(x_train, y_train)

# y_lr_train_pred = lr.predict(x_train)
# y_lr_test_pred = lr.predict(x_test)

# lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
# lr_train_r2 = r2_score(y_train, y_lr_train_pred)
# lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
# lr_test_r2 = r2_score(y_test, y_lr_test_pred)

# # -------------------------------
# # Random Forest Regressor Model
# # -------------------------------
# rf = RandomForestRegressor(n_estimators=100, random_state=100)
# rf.fit(x_train, y_train)

# y_rf_train_pred = rf.predict(x_train)
# y_rf_test_pred = rf.predict(x_test)

# rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
# rf_train_r2 = r2_score(y_train, y_rf_train_pred)
# rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
# rf_test_r2 = r2_score(y_test, y_rf_test_pred)

# # -------------------------------
# # Combine Results
# # -------------------------------
# results = pd.DataFrame([
#     ['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2],
#     ['Random Forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]
# ], columns=['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2'])

# print("\n✅ Model Evaluation Results:")
# print(results)

# # -------------------------------
# # Save models
# # -------------------------------
# joblib.dump(lr, 'linear_regression_model.pkl')
# joblib.dump(rf, 'random_forest_model.pkl')

# print("\n✅ Models saved as 'linear_regression_model.pkl' and 'random_forest_model.pkl'")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv('water_data.csv')

# Split features and target
X = df.drop('water_required', axis=1)
y = df['water_required']

# One-hot encode categorical features
X_encoded = pd.get_dummies(X)

# Save column names for later use during prediction
joblib.dump(X_encoded.columns.tolist(), 'model_columns.pkl')

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=100)

# Train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Save the model
joblib.dump(model, 'linear_regression_model.pkl')
print("✅ Model trained and saved successfully.")
