import psutil
import time
import random
from datetime import datetime
from utils.metrics import calculate_error_count

# initialize once
prev_net = psutil.net_io_counters()
prev_time = time.time()


def collect_metrics():
    global prev_net, prev_time

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    # Temperature
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            temperature = list(temps.values())[0][0].current
        else:
            # Fallback logic
            temperature = 30 + (cpu * 0.5) + (memory * 0.2) + random.uniform(0, 5)

    except:
        # Fallback logic
        temperature = 30 + (cpu * 0.5) + (memory * 0.2) + random.uniform(0, 5)

    # Clamp realistic range
    temperature = round(max(30, min(100, temperature)), 2)


    # Uptime
    uptime_seconds = int(time.time() - psutil.boot_time())

    # Network
    current_net = psutil.net_io_counters()
    current_time = time.time()

    net_sent = current_net.bytes_sent
    net_recv = current_net.bytes_recv

    upload_speed = (current_net.bytes_sent - prev_net.bytes_sent) / (current_time - prev_time)
    download_speed = (current_net.bytes_recv - prev_net.bytes_recv) / (current_time - prev_time)

    prev_net = current_net
    prev_time = current_time

    # Error Counter
    error_count = calculate_error_count(cpu, memory, temperature)

    data = {
        "timestamp": timestamp,
        "cpu_usage": cpu,
        "memory_usage": memory,
        "temperature": temperature,
        "uptime_seconds": uptime_seconds,
        "network_sent": net_sent,
        "network_received": net_recv,
        "upload_speed": upload_speed,
        "download_speed": download_speed,
        "error_count": error_count
    }

    return data

                                                                                
