def calculate_error_count(cpu, memory, temperature):
    error_count = 0

    if cpu > 90:
        error_count += 1
    if memory > 90:
        error_count += 1
    if temperature > 85:
        error_count += 1

    return error_count