from scripts.predict import predict_health

score, category, errors = predict_health(
    cpu=60,
    memory=10,
    temperature=0,
    uptime=12000,
    upload_speed=1200,
    download_speed=2400
)

print("Health Score:", score)
print("Category:", category)
print("Auto Error Count:", errors)
