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


# multiple select ka option dega
selected_timezone = st.multiselect(
    "Selected Timezone", TIME_ZONE, default=["UTC","Asia/Karachi"]
)

st.subheader("Selected Timezone")
# tz means time zone hy jo array m sari country k naam likhe howe
for tz in selected_timezone:
    # datetime.now ye current time dega zoneinfo means alag alag country ka time lakr dega
    # strftime ye method time ko sahi format m likh k dega %I ye meray current time ko am ya pm m convert kr rahi hy %p ka kam 24 hours format ko 12 hours format m convert kr rha hy
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")


st.subheader("Convert Time Between Timezones")

# time input time ki value deta hy select time dega
current_time = st.time_input("Current Time", value = datetime.now().time())


form_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)

if st.button("Convert Time"):
    # datetime ek module y jo current date or time dega combine different time zone ko combine kr k varaible m store kare
    dt = datetime.combine(datetime.today(), current_time, tzinfo= ZoneInfo(form_tz))

    converted_time = dt.astimezone(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    st.success(f"Converted Time in {to_tz}: {converted_time} ")