# 🖥️ AI System Health Analyzer

## 📌 Overview

AI System Health Analyzer is a machine learning-based system that monitors system performance metrics and predicts an overall **health score (0–100)**.

It analyzes parameters like CPU usage, memory usage, temperature, uptime, and network activity to determine system health in real time.

---

## 🚀 Features

* 📊 Real-time system monitoring
* 🤖 Machine learning-based health prediction
* 📈 Interactive dashboard using Streamlit
* ⚠️ Error tracking and anomaly insights
* 📉 Trend analysis (CPU, Memory, Health Score)

---

## 🧠 Model Inputs

The model uses the following features:

1. CPU Usage (%)
2. Memory Usage (%)
3. Temperature (°C)
4. Uptime (seconds)
5. Upload Speed (bytes/sec)
6. Download Speed (bytes/sec)
7. Error Count

---

## 📤 Output

* **Health Score (0–100)**

### 📊 Health Categories:

* **90 – 100 → Healthy ✅**
* **65 – 89 → Good 👍**
* **40 – 64 → Degrading ⚠️**
* **Below 40 → Critical ❌**

---

## ⚙️ Installation

### Step 1: Get the Project

You can either clone the repository or download it as a ZIP:

```bash
git clone <https://github.com/nikky-001/AI-System-Health-Analyzer>
cd ai-system-health-analyzer
```

---

### Step 2: Install Dependencies

Make sure you are in the **project root directory**, then run:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 1. Generate Dataset (Optional - First Time Only)

```bash
python -m scripts.generate_dataset
```

### 🔹 2. Clean Data

```bash
python -m scripts.data_cleaning
```

### 🔹 3. Train Model

```bash
python -m scripts.train_model
```

### 🔹 4. Run Prediction (CLI)

```bash
python main.py
```

### 🔹 5. Run UI Application (Popup)

```bash
python scripts/ui_app.py
```

### 🔹 6. Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Dashboard Features

* KPI metrics (CPU, Memory, Health Score)
* Time-based filtering (minutes)
* Trend visualization
* Network usage graphs
* Error distribution analysis

---

## 🏗️ Project Structure

```
ai-system-health-analyzer/
│
├── scripts/
│   ├── collector.py
│   ├── scorer.py
│   ├── generate_dataset.py
│   ├── data_cleaning.py
│   ├── train_model.py
│   ├── predict.py
│   └── ui_app.py
│
├── utils/
│   └── metrics.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── system_data.csv
│   └── clean_system_data.csv
│
├── models/
|   ├── health_model.onnx
│   ├── health_model.pkl
│   └── scaler.pkl
|
├── main.py
├── convert_to_onnx.py
├── .gitignore
├── requirements.txt
├── PROJECT_OVERVIEW.md
└── README.md
```

---

## 🔄 Workflow

1. Collect system metrics
2. Generate dataset
3. Clean data
4. Train model
5. Predict health score
6. Visualize using dashboard

---

## ⚠️ Important Notes

* Dataset generation is required only once initially
* Model should be retrained if new data is added
* Ensure feature consistency during prediction
* Error count and network speeds are derived features

---

## 🧪 Future Improvements

* Advanced anomaly detection with intelligent spike analysis
* Real-time alert system for critical health conditions
* Time-series forecasting for future health prediction
* Enhanced UI/visualization for live system monitoring
* Optimization for low-resource embedded systems

---
