import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
import pandas as pd
from tkinter import messagebox
from scripts.predict import predict_health

df = pd.read_csv("data/system_data.csv")

def show_result(score, category, avg_score, reasons, suggestions):

    popup = tk.Toplevel()
    popup.title("System Health Result")
    popup.geometry("420x380")

    # Color Logic
    color_map = {
        "Healthy": "green",
        "Good": "blue",
        "Degrading": "orange",
        "Critical": "red"
    }

    color = color_map.get(category, "black")

    tk.Label(popup, text="System Health Result",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(popup, text=f"Health Score: {score}",
             fg=color, font=("Arial", 14, "bold")).pack()

    tk.Label(popup, text=f"Category: {category}",
             fg=color, font=("Arial", 14, "bold")).pack()

    tk.Label(popup, text=f"Average Benchmark: {avg_score}",
             font=("Arial", 11)).pack(pady=5)

    tk.Label(popup, text="Why this category?",
             font=("Arial", 12, "bold")).pack()

    for r in reasons:
        tk.Label(popup, text="• " + r).pack()

    tk.Label(popup, text="Suggestions:",
             font=("Arial", 12, "bold")).pack(pady=5)

    for s in suggestions:
        tk.Label(popup, text="• " + s).pack()

def run_prediction():

    cpu = int(cpu_entry.get())
    memory = int(mem_entry.get())
    temp = int(temp_entry.get())
    uptime = int(uptime_entry.get())
    upload = int(upload_entry.get())
    download = int(download_entry.get())

    score, category, errors = predict_health(
        cpu, memory, temp, uptime, upload, download
    )

    avg_score = round(df["health_score"].mean()) if "health_score" in df.columns else "N/A"

    reasons = []
    suggestions = []

    if cpu > 80:
        reasons.append("High CPU Usage")
        suggestions.append("Close heavy applications")

    if memory > 80:
        reasons.append("High Memory Usage")
        suggestions.append("Restart unused apps")

    if temp > 75:
        reasons.append("High Temperature")
        suggestions.append("Improve cooling")

    if not reasons:
        reasons.append("Metrics within safe limits")
        suggestions.append("Maintain monitoring")

    show_result(score, category, avg_score, reasons, suggestions)


root = tk.Tk()
root.title("System Health Checker")
root.geometry("380x350")

tk.Label(root, text="Enter System Metrics",
         font=("Arial", 14, "bold")).pack(pady=10)

def create_field(label):
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    return entry

cpu_entry = create_field("CPU %")
mem_entry = create_field("Memory %")
temp_entry = create_field("Temperature")
uptime_entry = create_field("Uptime Seconds")
upload_entry = create_field("Upload Speed")
download_entry = create_field("Download Speed")

tk.Button(root, text="Check Health",
          command=run_prediction,
          bg="black", fg="white").pack(pady=15)

root.mainloop()
