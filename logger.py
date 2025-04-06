import json
from datetime import datetime
import os

LOG_FILE = "log.json"

def get_input(prompt):
    return input(prompt + " ")

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def save_log(log_data):
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

def main():
    print("🏃‍♂️ Trail Logger")

    entry = {
        "trail": get_input("📍 Trail name:"),
        "date": get_input("📆 Date (YYYY-MM-DD):") or datetime.today().strftime("%Y-%m-%d"),
        "distance_mi": float(get_input("📏 Distance (miles):")),
        "elevation_gain_ft": int(get_input("⬆️ Vertical gain (feet):")),
        "effort": int(get_input("⚡ Effort level (1–10):")),
        "vibe": get_input("🌤️ Vibe summary:"),
    }

    log = load_log()
    log.append(entry)
    save_log(log)

    print("\n✅ Entry saved!")

if __name__ == "__main__":
    main()
