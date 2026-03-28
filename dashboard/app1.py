import sys
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

df = pd.read_csv("data/system_data.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

import streamlit as st

time_range = st.selectbox(
    "Select Time Range",
    ["Last 1 Hour", "Last 24 Hours", "Last 7 Days", "Last 30 Days"]
)

now = df["timestamp"].max()

if time_range == "Last 1 Hour":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(hours=1)]

elif time_range == "Last 24 Hours":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(days=1)]
 
elif time_range == "Last 7 Days":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(days=7)]

elif time_range == "Last 30 Days":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(days=30)]

    st.subheader("CPU Usage Trend")

st.line_chart(
    filtered_df.set_index("timestamp")["cpu_usage"]
)

st.subheader("System Metrics Trend")

st.line_chart(
    filtered_df.set_index("timestamp")[["cpu_usage", "memory_usage", "health_score"]]
)

hourly_data = filtered_df.resample("1H", on="timestamp").mean()

start_date, end_date = st.date_input(
    "Select Date Range",
    [df["timestamp"].min(), df["timestamp"].max()]
)

filtered = df[(df["timestamp"] >= str(start_date)) & (df["timestamp"] <= str(end_date))]

st.line_chart(
    filtered.set_index("timestamp")["cpu_usage"]
)

import numpy as np

# Calculate mean and std
mean_cpu = filtered_df["cpu_usage"].mean()
std_cpu = filtered_df["cpu_usage"].std()

# Z-score
filtered_df["cpu_zscore"] = (filtered_df["cpu_usage"] - mean_cpu) / std_cpu

# Mark anomalies
filtered_df["cpu_anomaly"] = filtered_df["cpu_zscore"].abs() > 2

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Normal points
normal = filtered_df[filtered_df["cpu_anomaly"] == False]
ax.plot(normal["timestamp"], normal["cpu_usage"], label="Normal")

# Anomaly points
anomaly = filtered_df[filtered_df["cpu_anomaly"] == True]
ax.scatter(anomaly["timestamp"], anomaly["cpu_usage"], label="Anomaly", marker="o")

ax.set_title("CPU Usage with Anomalies")
ax.set_xlabel("Time")
ax.set_ylabel("CPU Usage")

st.pyplot(fig)

st.write("## 🔮 Predict System Health")

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        cpu = st.number_input("CPU Usage %", 0, 100, 20)
        memory = st.number_input("Memory Usage %", 0, 100, 30)

    with col2:
        temperature = st.number_input("Temperature °C", 0, 120, 40)
        uptime = st.number_input("Uptime Seconds", 0, 999999, 10000)

    with col3:
        upload = st.number_input("Upload Speed", 0, 100000, 1000)
        download = st.number_input("Download Speed", 0, 100000, 2000)

    submitted = st.form_submit_button("Predict Health")

if submitted:
    score, category, errors = predict_health(
        cpu, memory, temperature, uptime, upload, download
    )

    avg_score = round(df["health_score"].mean()) if "health_score" in df.columns else "N/A"

    # -------- EXPLANATION LOGIC --------
    reasons = []
    suggestions = []

    if cpu > 80:
        reasons.append("High CPU Usage")
        suggestions.append("Close heavy applications")

    if memory > 80:
        reasons.append("High Memory Usage")
        suggestions.append("Restart unused programs")

    if temperature > 75:
        reasons.append("High Temperature")
        suggestions.append("Improve cooling / clean vents")

    if not reasons:
        reasons.append("System metrics are within safe limits")
        suggestions.append("Maintain regular monitoring")

    # -------- RESULT CARD --------
    st.markdown("---")
    st.markdown("### 🧾 Prediction Result")

    st.success(f"**Health Score:** {score}")
    st.info(f"**Category:** {category}")
    st.write(f"**Average System Score Benchmark:** {avg_score}")

    st.write("**Why this Category?**")
    for r in reasons:
        st.write("•", r)

    st.write("**Suggestions to Improve:**")
    for s in suggestions:
        st.write("•", s)