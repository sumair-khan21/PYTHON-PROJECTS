import streamlit as st  # Streamlit module jo interactive web apps banane ke liye use hota hai
import pandas as pd  # Data manipulation ke liye Pandas library
import datetime  # Date handle karne ke liye
import csv  # CSV files read aur write karne ke liye
import os  # File operations handle karne ke liye

# MOOD_FILE ek constant variable hai jo mood ko store karne wali file ka naam hai
MOOD_FILE = "mood_log.csv"

# Function jo mood ka data load karega
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        # Agar file exist nahi karti ya empty hai toh ek empty dataframe return hoga
        return pd.DataFrame(columns=["Date", "Mood"])
    # Agar file mojood hai toh usko read kar ke dataframe return karega
    return pd.read_csv(MOOD_FILE)

# Function jo user ka mood save karega
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)  # Check karega file exist karti hai ya nahi
    
    # "a" mode ka matlab hai file ko append mode me open karna taki naye records add ho sakein
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)  # Writer function CSV file me data likhne ke liye
        
        # Agar file exist nahi karti ya empty hai toh headers likhne ke liye ye condition hai
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])  # CSV file me headers add kar raha hai
        
        writer.writerow([date, mood])  # Naya data likh raha hai

# Streamlit ka title jo app ka heading show karega
st.title("Mood Tracker")

# Aaj ki date nikal raha hai
today = datetime.date.today()

# Subheading show karega
st.subheader("How are you feeling today?")

# User se mood select karwane ke liye dropdown box
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Agar user "Log Mood" button click karega toh data save hoga
if st.button("Log Mood"):
    save_mood_data(today, mood)  # Function call jo data save karega
    st.success("Mood Logged Successfully!")  # Success message show karega

# Pehle se saved mood data ko load kar raha hai
data = load_mood_data()

# Debugging step: Check karega ke data sahi load ho raha hai ya nahi
st.write("Data Loaded:", data)

# Agar data empty nahi hai toh usko analyze karega
if not data.empty:
    st.subheader("Mood Trends Over Time")  # Subheading show karega
    
    # ["Date"] ye CSV file me ek column hai
    # to_datetime ka use string ko date format me convert karne ke liye hota hai
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')  # Error handling ke saath conversion
    
    # groupby function use kar ke har mood ka count nikal raha hai
    mood_counts = data.groupby("Mood").count()["Date"]
    
    # Mood ka data bar chart ke form me show karega
    st.bar_chart(mood_counts)
