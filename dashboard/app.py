import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.predict import predict_health

st.set_page_config(page_title="AI System Health Analyzer", layout="wide")
st.title("🖥️ AI System Health Analyzer")
st.subheader("System Monitoring Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/system_data.csv")

df = load_data()
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

# KPI's
latest = df.iloc[-1]

cpu_avg, cpu_min, cpu_max = df["cpu_usage"].mean(), df["cpu_usage"].min(), df["cpu_usage"].max()
mem_avg, mem_min, mem_max = df["memory_usage"].mean(), df["memory_usage"].min(), df["memory_usage"].max()
if "health_score" in df.columns:
    score_avg, score_min, score_max = df["health_score"].mean(), df["health_score"].min(), df["health_score"].max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage (%)", round(latest["cpu_usage"]), delta=round(latest["cpu_usage"]-cpu_avg))
    st.caption(f"Avg: {round(cpu_avg)} | Min: {round(cpu_min)} | Max: {round(cpu_max)}")

with col2:
    st.metric("Memory Usage (%)", round(latest["memory_usage"]), delta=round(latest["memory_usage"]-mem_avg))
    st.caption(f"Avg: {round(mem_avg)} | Min: {round(mem_min)} | Max: {round(mem_max)}")

with col3:
    if "health_score" in df.columns:
        st.metric("Health Score", round(latest["health_score"]), delta=round(latest["health_score"]-score_avg))
        st.caption(f"Avg: {round(score_avg)} | Min: {round(score_min)} | Max: {round(score_max)}")
    else:
        st.metric("Health Score", "N/A")

# Resampling for trends
time_range = st.selectbox(
    "Select Time Range",
    ["Last 1 Hour", "Last 6 Hours", "Last 24 Hours", "Last 7 Days", "Last 30 Days"]
)

now = df["timestamp"].max()

if time_range == "Last 1 Hour":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(hours=1)]

elif time_range == "Last 6 Hours":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(hours=6)]

elif time_range == "Last 24 Hours":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(days=1)]

elif time_range == "Last 7 Days":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(days=7)]

elif time_range == "Last 30 Days":
    filtered_df = df[df["timestamp"] >= now - pd.Timedelta(days=30)]

resampled_df = filtered_df.set_index("timestamp").resample("5min").mean().dropna()

cpu_mean = resampled_df["cpu_usage"].mean()
cpu_std = resampled_df["cpu_usage"].std()

resampled_df["cpu_anomaly"] = (
    (resampled_df["cpu_usage"] - cpu_mean).abs() > 2 * cpu_std
)

cpu_spikes = resampled_df["cpu_anomaly"].sum()

st.metric("CPU Spikes Detected in Selected Period", int(cpu_spikes))

# Trends
st.write("## Usage & Health Trends")
col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots()

    ax.plot(resampled_df.index, resampled_df["cpu_usage"], label="CPU Usage")

    spikes = resampled_df[resampled_df["cpu_anomaly"]]

    ax.scatter(
        spikes.index,
        spikes["cpu_usage"],
        color="red",
        label="Spike"
    )

    ax.set_xlabel("Time")
    ax.set_ylabel("CPU %")
    ax.set_title("CPU Usage Trend with Spikes")

    ax.legend()

    st.pyplot(fig)   

with col2:
    st.line_chart(resampled_df["memory_usage"])
    st.caption("Memory Usage Trend (1-min avg)")

with col3:
    if "health_score" in resampled_df.columns:
        st.line_chart(resampled_df["health_score"])
        st.caption("Health Score Trend (1-min avg)")

# Network trends
st.write("## Network Traffic Trends")
col1, col2 = st.columns(2)

with col1:
    st.line_chart(resampled_df[["network_sent", "network_received"]])
    st.caption("Network Sent & Received (1-min avg)")

with col2:
    st.line_chart(resampled_df[["upload_speed", "download_speed"]])
    st.caption("Upload & Download Speed (1-min avg)")

# Histograms
st.write("## CPU and Memory Distribution")
col1, col2 = st.columns(2)

with col1:
    st.write("### CPU Usage Histogram")
    fig, ax = plt.subplots()
    bins = np.arange(0, 105, 5)
    ax.hist(df["cpu_usage"], bins=bins, color="skyblue", edgecolor="black")
    ax.set_xlabel("CPU Usage (%)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

with col2:
    st.write("### Memory Usage Histogram")
    fig, ax = plt.subplots()
    bins = np.arange(0, 105, 5)
    ax.hist(df["memory_usage"], bins=bins, color="lightgreen", edgecolor="black")
    ax.set_xlabel("Memory Usage (%)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Errors & Health
st.write("## Errors & Health Distribution")
col1, col2 = st.columns(2)  

with col1:
    st.write("### Error Count Histogram")
    fig, ax = plt.subplots()
    bins = np.arange(0, df["error_count"].max() + 1, 1)
    ax.hist(df["error_count"], bins=bins, color=["#FF9999"], edgecolor="black")
    ax.set_xlabel("Error Count")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

with col2:
    if "health_score" in df.columns:
        st.write("### Health Score Histogram")
        fig, ax = plt.subplots()
        bins = np.arange(0, 105, 5)
        ax.hist(df["health_score"], bins=bins, color="#FFD700", edgecolor="black")
        ax.set_xlabel("Health Score")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)




