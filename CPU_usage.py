import psutil

# Define the CPU usage threshold (e.g., 80%)
cpu_threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        # Get the current CPU usage as a percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        if cpu_usage > cpu_threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
except KeyboardInterrupt:
    print("Monitoring stopped due to user interruption.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
