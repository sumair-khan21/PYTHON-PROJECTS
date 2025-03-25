import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


TIME_ZONE = [
       "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone App")

selected_timezone = st.multiselect(
    "Selected Timezone", TIME_ZONE, default=["UTC","Asia/Karachi"]
)

st.subheader("Selected Timezone")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")


st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value = datetime.now().time())

form_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo= ZoneInfo(form_tz))

    converted_time = dt.astimezone(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    st.success(f"Converted Time in {to_tz}: {converted_time} ")