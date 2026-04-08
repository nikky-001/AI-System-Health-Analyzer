import joblib
from sklearn.pipeline import Pipeline
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Load model & scaler
model = joblib.load("models/health_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Create pipeline
pipeline = Pipeline([
    ("scaler", scaler),
    ("model", model)
])

# Define input shape (7 features)
initial_type = [('float_input', FloatTensorType([None, 7]))]

# Convert to ONNX
onnx_model = convert_sklearn(pipeline, initial_types=initial_type)

# Save model
with open("models/health_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("✅ ONNX model created successfully!")