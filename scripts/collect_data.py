import psutil
import time
from datetime import datetime
import csv
import os

file_path = "data/system_data.csv"

# Create header if file doesn't exist
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
            "error_count"
        ])

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    # Temperature (may not work on all Windows laptops)
    try:
        temps = psutil.sensors_temperatures()
        temperature = list(temps.values())[0][0].current if temps else 0
    except:
        temperature = 0

    # Uptime
    uptime_seconds = int(time.time() - psutil.boot_time())

    # Network
    net = psutil.net_io_counters()
    net_sent = net.bytes_sent
    net_recv = net.bytes_recv

    # Error Counter Logic
    error_count = 0

    if cpu > 90 or memory > 90 or temperature > 85:
        error_count = 1

    print("Time:", timestamp)
    print("CPU:", cpu)
    print("Memory:", memory)
    print("Temp:", temperature)
    print("Errors:", error_count)
    print("-----------------------")

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            timestamp,
            cpu,
            memory,
            temperature,
            uptime_seconds,
            net_sent,
            net_recv,
            error_count
        ])

    time.sleep(5)

