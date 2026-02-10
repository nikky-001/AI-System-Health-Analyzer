import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

#Load Data
file_path = "data/clean_system_data.csv"
df = pd.read_csv(file_path)

print("Dataset Loaded")
print("Shape:", df.shape)
print(df.head())

# Drop unnecessary columns
columns_to_drop = ["timestamp", "network_sent", "network_received"]
df = df.drop(columns=columns_to_drop, errors="ignore")

# Separate Features and Target
X = df.drop("health_score", axis=1)
y = df["health_score"]

print("Feature Columns:", X.columns.tolist())
print("Target Column:", y.name)

#Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Size:", X_train.shape)
print("Testing Size:", X_test.shape)

#Feature Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling Done")

#Model Training
model = RandomForestRegressor(random_state=42)

model.fit(X_train_scaled, y_train)

print("Model Training Completed")

#Model Evaluation
y_pred = model.predict(X_test_scaled)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("\nModel Performance:")
print("R2 Score:", r2)
print("MAE:", mae)
print("RMSE:", rmse)

#Save Model
model_folder = "models"
os.makedirs(model_folder, exist_ok=True)

model_path = os.path.join(model_folder, "health_model.pkl")

joblib.dump(model, model_path)

print("Model Saved At:", model_path)

scaler_path = os.path.join(model_folder, "scaler.pkl")
joblib.dump(scaler, scaler_path)

print("Scaler Saved At:", scaler_path)

