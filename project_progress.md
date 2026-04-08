1. Project Overview

The AI System Health Analyzer is designed to monitor system performance metrics such as CPU usage, memory usage, temperature, and other system parameters. The goal of the project is to analyze system behavior, detect anomalies, and visualize performance trends through an interactive dashboard.

2. Dataset Generation

Initially, a system metrics dataset was generated at an interval of 5 seconds to capture system performance parameters such as CPU usage, memory usage, and other system statistics.

3. Data Cleaning and Preprocessing

The generated dataset was cleaned to remove inconsistencies and prepare the data for model training and analysis. Data preprocessing ensured that the dataset was structured properly and suitable for further processing.

4. Data Visualization and Initial Dashboard

After cleaning the dataset, a prototype dashboard was developed to visualize system performance metrics. The dashboard includes:

*Average CPU usage

*Average memory usage

*System health score

*Trend graphs for CPU and memory

*Histograms for metric distribution

*Pie chart for error count

These visualizations help in understanding system performance trends and identifying abnormal behavior.

5. Model Development and Training

A machine learning model was developed and trained using the processed dataset to analyze system health metrics and detect anomalies based on system performance patterns.

6. Prediction Interface

A simple user interface was created to allow interaction with the trained model. The interface enables users to run predictions and observe the system health analysis results.

7. Issue Identified – Temperature Data

During development, it was observed that system temperature values were not being captured on Windows systems, which could affect the accuracy of model training.

8. Dataset Regeneration with Improved Logic

To address this limitation, the dataset was regenerated with an improved logic that simulates temperature values based on CPU usage and memory utilization.
Additionally, the data collection interval was modified from 5 seconds to 2 minutes to create a more realistic monitoring dataset.

9. Dashboard Enhancements – Custom Time Range

The dashboard was updated to allow customized time-based trend analysis, enabling users to view system performance for:

Last 24 days

Last 7 days

Last 24 hours

Last 6 hours

Last 1 hour

10. Anomaly Detection Visualization

A feature was added to highlight CPU spikes within the selected time period, helping users identify sudden increases in CPU usage.

11. CPU Spike Counting

Additional logic was implemented to count the number of CPU spikes detected within the selected time range, providing better insight into system workload patterns.

12. Modular Project Structure

The project code was organized into separate modules for data processing, prediction logic, and dashboard visualization, improving code maintainability and scalability.

13. Dashboard Development

An interactive and dynamic dashboard was developed to visualize system metrics, health score trends, and network activity with customizable time-based filtering for enhanced monitoring and analysis.