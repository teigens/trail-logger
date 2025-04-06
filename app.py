import streamlit as st
import json
import os
import pandas as pd

LOG_FILE = "log.json"

# Load data
def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

log = load_log()

# Add the Entry Form to the Sidebar
from datetime import date

def save_entry(entry):
    log = load_log()
    log.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)
    st.success("✅ Trail run logged!")
    st.rerun()




# Convert to DataFrame
df = pd.DataFrame(log)

st.title("🏃‍♂️ Trail Log Dashboard")

if df.empty:
    st.warning("No trail entries found.")
    st.stop()

# Sidebar Form
with st.sidebar.form("log_entry"):
    st.header("📝 Log a New Trail Run")

    trail = st.text_input("Trail name")
    run_date = st.date_input("Date", value=date.today())
    distance = st.number_input("Distance (miles)", min_value=0.0, step=0.1)
    gain = st.number_input("Elevation gain (ft)", min_value=0)
    effort = st.slider("Effort (1–10)", min_value=1, max_value=10)
    vibe = st.text_area("Vibe summary")

    submitted = st.form_submit_button("Save Entry")

    if submitted:
        new_entry = {
            "trail": trail,
            "date": run_date.strftime("%Y-%m-%d"),
            "distance_mi": distance,
            "elevation_gain_ft": gain,
            "effort": effort,
            "vibe": vibe
        }
        save_entry(new_entry)


# Filters
with st.sidebar:
    st.header("🔍 Filter Log")
    trail_filter = st.text_input("Trail name contains")
    min_effort = st.slider("Minimum effort", 1, 10, 1)
    max_distance = st.number_input("Max distance (mi)", min_value=0.0, value=50.0)

# Apply filters
filtered = df[
    (df["effort"] >= min_effort)
    & (df["distance_mi"] <= max_distance)
    & (df["trail"].str.lower().str.contains(trail_filter.lower() if trail_filter else "", na=False))
]


st.subheader(f"📝 {len(filtered)} Entries Found")
st.dataframe(filtered)

# Summary stats
st.subheader("📊 Summary")
st.metric("Total Miles", round(filtered["distance_mi"].sum(), 2))
st.metric("Total Elevation Gain (ft)", int(filtered["elevation_gain_ft"].sum()))
st.metric("Average Effort", round(filtered["effort"].mean(), 1))

# Distance over time chart
st.subheader("📆 Distance Over Time")
df_chart = filtered.copy()
df_chart["date"] = pd.to_datetime(df_chart["date"])
df_chart = df_chart.sort_values("date")


# Effort vs Elevation chart
st.line_chart(df_chart.set_index("date")["distance_mi"])    
st.subheader("⚡ Effort vs Elevation Gain")
st.scatter_chart(df_chart[["elevation_gain_ft", "effort"]])

