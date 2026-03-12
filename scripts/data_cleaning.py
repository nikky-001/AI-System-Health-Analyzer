import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load data 
file_path = "data/system_data.csv"
df = pd.read_csv(file_path)

print("Initial Shape:", df.shape)
print(df.head())

# Remove completely empty rows
df.dropna(how="all", inplace=True)

# Fill missing values with 0
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)

print("Duplicates Removed:", before - after)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nStatistics Summary:")
print(df.describe())

#Corealation Analysis
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()


# CPU Usage Distribution
plt.figure()
df["cpu_usage"].hist()
plt.title("CPU Usage Distribution")
plt.xlabel("CPU Usage")
plt.ylabel("Frequency")
plt.show()

# Memory Usage Distribution
plt.figure()
df["memory_usage"].hist()
plt.title("Memory Usage Distribution")
plt.xlabel("Memory Usage")
plt.ylabel("Frequency")
plt.show()

# Error Count Frequency
plt.figure()
df["error_count"].value_counts().plot(kind="bar")
plt.title("Error Count Frequency")
plt.xlabel("Error Value")
plt.ylabel("Count")
plt.show()

# Health Score Distribution
if "health_score" in df.columns:
    plt.figure()
    df["health_score"].hist()
    plt.title("Health Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()


clean_path = "data/clean_system_data.csv"
df.to_csv(clean_path, index=False)

print("\nClean dataset saved at:", clean_path)
print("Final Shape:", df.shape)


