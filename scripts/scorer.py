def calculate_health_score(data):
    score = 100

    cpu = data["cpu_usage"]
    memory = data["memory_usage"]
    temperature = data["temperature"]
    upload = data["upload_speed"]
    download = data["download_speed"]
    error = data["error_count"]
    uptime = data["uptime_seconds"]

    # CPU penalty
    if cpu > 80:
        score -= 25
    elif cpu > 60:
        score -= 15
    elif cpu > 40:
        score -= 5

    # Memory penalty
    if memory > 80:
        score -= 25
    elif memory > 60:
        score -= 15
    elif memory > 40:
        score -= 5

    # Temperature penalty (ignore 0)
    if temperature > 0:
        if temperature > 80:
            score -= 20
        elif temperature > 65:
            score -= 10
        elif temperature > 50:
            score -= 5

    # Network speed penalty
    if upload > 500000 or download > 500000:
        score -= 5

    # Error penalty 
    if error > 0:
        score -= 30

    # Uptime penalty
    if uptime > 86400: 
        score -= 2

    # Clamp score between 0 and 100
    score = max(0, min(100, score))

    return score
