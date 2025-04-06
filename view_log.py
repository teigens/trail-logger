import json
from tabulate import tabulate
import os

LOG_FILE = "log.json"

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def main():
    log = load_log()
    if not log:
        print("No entries yet.")
        return

    table = []
    for entry in log:
        table.append([
            entry["date"],
            entry["trail"],
            entry["distance_mi"],
            entry["elevation_gain_ft"],
            entry["effort"],
            entry["vibe"]
        ])

    headers = ["Date", "Trail", "Miles", "Gain (ft)", "Effort", "Vibe"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
