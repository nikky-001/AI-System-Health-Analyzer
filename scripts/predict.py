import joblib
import pandas as pd
from utils.metrics import calculate_error_count

# Load model and scaler
model = joblib.load("models/health_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def predict_health(cpu, memory, temperature, uptime, upload_speed, download_speed):

    # AUTO ERROR COUNT
    error_count = calculate_error_count(cpu, memory, temperature)

    # Create dataframe
    data = pd.DataFrame([{
        "cpu_usage": cpu,
        "memory_usage": memory,
        "temperature": temperature,
        "uptime_seconds": uptime,
        "upload_speed": upload_speed,
        "download_speed": download_speed,
        "error_count": error_count
    }])

    # Scale
    data_scaled = scaler.transform(data)

    # Predict
    score =round( model.predict(data_scaled)[0])

    # Category
    if score >= 90:
        category = "Healthy"
    elif score >= 65:
        category = "Good"
    elif score >= 40:
        category = "Degrading"
    else:
        category = "Critical"

    return score, category, error_count


