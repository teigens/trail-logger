import json
import os

LOG_FILE = "log.json"

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def summarize(log):
    total_miles = sum(entry["distance_mi"] for entry in log)
    total_gain = sum(entry["elevation_gain_ft"] for entry in log)
    total_effort = sum(entry["effort"] for entry in log)
    count = len(log)
    avg_effort = round(total_effort / count, 1) if count > 0 else 0

    print("\n📊 Trail Log Summary")
    print("----------------------")
    print(f"📝 Entries logged:       {count}")
    print(f"📏 Total distance (mi):  {total_miles}")
    print(f"⬆️ Total elevation gain: {total_gain} ft")
    print(f"⚡ Avg. effort level:     {avg_effort}")

def main():
    log = load_log()
    if not log:
        print("⚠️ No entries found.")
        return
    summarize(log)

if __name__ == "__main__":
    main()
