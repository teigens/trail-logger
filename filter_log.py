import json
import os

LOG_FILE = "log.json"

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def filter_log(log, trail_name=None, min_effort=None, max_distance=None):
    results = []
    for entry in log:
        if trail_name and trail_name.lower() not in entry["trail"].lower():
            continue
        if min_effort and entry["effort"] < min_effort:
            continue
        if max_distance and entry["distance_mi"] > max_distance:
            continue
        results.append(entry)
    return results

def print_results(results):
    if not results:
        print("❌ No entries matched.")
        return

    print(f"\n🔍 Found {len(results)} matching entries:\n")
    for entry in results:
        print(f"{entry['date']} - {entry['trail']} - {entry['distance_mi']} mi - {entry['elevation_gain_ft']} ft - Effort {entry['effort']}")
        print(f"📝 {entry['vibe']}")
        print("-" * 40)

def main():
    log = load_log()
    if not log:
        print("⚠️ No entries found.")
        return

    print("🔍 Search your trail log")
    trail = input("Trail name (leave blank to skip): ")
    min_effort = input("Min effort (1–10, blank to skip): ")
    max_distance = input("Max distance (miles, blank to skip): ")

    # Convert inputs to proper types if provided
    min_effort = int(min_effort) if min_effort else None
    max_distance = float(max_distance) if max_distance else None

    results = filter_log(log, trail_name=trail, min_effort=min_effort, max_distance=max_distance)
    print_results(results)

if __name__ == "__main__":
    main()
