import psutil
import json
import logging
from datetime import datetime

logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_system_health():
    try:
        data = {
            "timestamp": datetime.now().isoformat(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent
        }
        return data
    except Exception as e:
        logging.error(f"Error collecting system health: {e}")
        return None

def save_to_json(data):
    try:
        with open("system_health.json", "a") as f:
            f.write(json.dumps(data) + "\n")
    except Exception as e:
        logging.error(f"Error saving JSON: {e}")

def main():
    health = get_system_health()
    if health:
        print("System Health Report:")
        print(json.dumps(health, indent=4))
        logging.info("System health collected successfully.")
        save_to_json(health)
    else:
        print("Failed to collect system health.")

if __name__ == "__main__":
    main()






















































































































