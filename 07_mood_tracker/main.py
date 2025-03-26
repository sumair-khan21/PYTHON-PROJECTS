# import streamlit as st
# import pandas as pd # data manipulation
# import datetime #handle date
# import csv # for reading and writing csv files
# import os # for file operations

# # mood file constant varaible isko mne samll isliye  nhi likha k ye constant file hy ye file change nhi hogi lekin iska data change hoga
# MOOD_FILE = "mood_log.csv"

# def load_mood_data():
#     if not os.path.exists(MOOD_FILE):
#         # dataframe pandas ka module hy ye hamray data ko sequence se kr deta hy row column wise
#         return pd.DataFrame(columns=["Date","Mood"])
#     # readcsv hamaray file k data kor read karegi ye bhi pandas ka module hy
#     return pd.read_csv(MOOD_FILE)


# def save_mood_data(date, mood):
#     # with hamaray data ko insert kr rha save kr rha hy csv file m "a" means append next line m data data ho rha or file ye ek varaible hy
#     with open(MOOD_FILE, "a") as file:
 
# #  writer function file k ander data ko write kr rha hy
#          writer = csv.writer(file)
     
#          writer.writerow([date, mood])
         
# st.title("Mood Tracker")

# today = datetime.date.today()

# st.subheader("How are you feeling today?")

# mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry","Neutral"])

# if st.button("Log Mood"):
#     save_mood_data(today, mood)
    
#     st.success("Mood Logged Successfully!")
    
# data = load_mood_data()

# if not data.empty:
    
#     st.subheader("Mood Trends Over Time")
    
# # ["Date"] ye csv ki file m key ka naam hy
# # to_datetime jo string m arha hy isko object m convert kr rha hy phle data ka vairble aya phr column ka name Date
#     data["Date"] = pd.to_datetime(data["Date"])
    
#     # groupby check karega k user ka mood kis din kesa ta
#     mood_counts = data.groupby("Mood").count()["Date"]
    
#     # bar chart means row and columns
#     st.bar_chart(mood_counts)
    
    
    
    
    
    
    
    
    
    
    
    
import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])  # Ensure headers exist
        writer.writerow([date, mood])

st.title("Mood Tracker")

today = datetime.date.today()
st.subheader("How are you feeling today?")
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

data = load_mood_data()

# Debugging Step
st.write("Data Loaded:", data)

if not data.empty:
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')  # Prevent errors if column format is wrong
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     import streamlit as st # For creating web interface
# import pandas as pd # For data manipulation
# import datetime # For handling dates
# import csv # For reading and writing CSV file
# import os # For file operations

# # Define the file name for storing mood data
# MOOD_FILE = "mood_log.csv"

# # Function to read mood data from the CSV file
# def load_mood_data():
#     # Check if the file exists
#     if not os.path.exists(MOOD_FILE):
#         # If no file, create empty DataFrame with columns
#         return pd.DataFrame(columns=["Date", "Mood"])
#     # Read and return existing mood data
#     return pd.read_csv(MOOD_FILE)

# # Function to add new mood entry to CSV file
# def save_mood_data(date, mood):
#     # Open file in append mode
#     with open(MOOD_FILE, "a") as file:

#         # Create CSV writer
#         writer = csv.writer(file)

#         # Add new mood entry
#         writer.writerow([date, mood])

# # Streamlit app title
# st.title("Mood Tracker")

# # Get today's date
# today = datetime.date.today()

# # Create subheader for mood input
# st.subheader("How are your feeling today?")

# # Create dropdown for mood selection
# mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# # Create button to save mood
# if st.button("Log Mood"):
    
#     # Save mood when button is clicked
#     save_mood_data(today, mood)

#     # Show success message
#     st.success("Mood Logged Successfully!")

# # Load existing mood data
# data = load_mood_data()

# # If there is data to display
# if not data.empty:

#     # Create section for Visualization
#     st.subheader("Mood Trends Over Time")

#     # Convert date stings to datetime Objects
#     data["Date"] = pd.to_datetime(data["Date"])

#     # Count frequency of each mood
#     mood_counts = data.groupby("Mood").count()["Date"]

#     # Display bar chart of mood frequencies
#     st.bar_chart(mood_counts)

#     # Build with love by Asharib Ali
#     st.write("Build with ❤️ by [Asharib Ali](https://github.com/AsharibAli)")

    