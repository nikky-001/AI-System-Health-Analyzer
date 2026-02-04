import csv
import os
import time
from collector import collect_metrics
from scorer import calculate_health_score

file_path = "data/system_data.csv"

# Create header if not exists
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp",
            "cpu_usage",
            "memory_usage",
            "temperature",
            "uptime_seconds",
            "network_sent",
            "network_received",
            "upload_speed",
            "download_speed",
            "error_count",
            "health_score"
        ])

print("Collecting training data... Press CTRL+C to stop.")

while True:
    data = collect_metrics()
    score = calculate_health_score(data)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            data["timestamp"],
            data["cpu_usage"],
            data["memory_usage"],
            data["temperature"],
            data["uptime_seconds"],
            data["network_sent"],
            data["network_received"],
            data["upload_speed"],
            data["download_speed"],
            data["error_count"],
            score
        ])

    time.sleep(5)
