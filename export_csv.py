import json
import csv
import os

LOG_FILE = "log.json"
CSV_FILE = "log.csv"

def load_log():
    if os.path.exists(LOG_FILE):
        print(f"📂 Found {LOG_FILE}")
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    print(f"❌ {LOG_FILE} not found.")
    return []

def export_to_csv(log_data):
    if not log_data:
        print("⚠️ No entries to export.")
        return

    try:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=log_data[0].keys())
            writer.writeheader()
            writer.writerows(log_data)
        print(f"✅ Exported {len(log_data)} entries to {CSV_FILE}")
    except Exception as e:
        print(f"❌ Error exporting CSV: {e}")

def main():
    print("🚀 Starting export...")
    log_data = load_log()
    export_to_csv(log_data)
    print("📁 Current directory:", os.getcwd())

if __name__ == "__main__":
    main()
