import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    # random number generate krta hy or randint kaha se ka tk krna ye handle krta hy
    return random.randint(1, 1000)


st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your Money....")
    time.sleep(3)    
    amount = generate_money()
    st.success(f"You made: ${amount}!")
    

def fetch_side_hustle():
    try:
        reponse = requests.get(
            "https://fastapi-api.vercel.app/side_hustles"
        )
        if reponse.status_code == 200:
            hustles = reponse.json()
            return hustles["side_hustle"]
        else:
            "Freelancing"
        
    except:
        return "Something went wrong!"
    
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)


def fetch_money_quotes():
    try:
        reponse = requests.get(
            "https://fastapi-api.vercel.app/money_quotes"
        )
        if reponse.status_code == 200:
            quotes = reponse.json()
            return quotes["money_quote"]
        else:
            return "Money is the root of all evil!"
    
    except:
        "Something went wrong"
    
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.info(quote)