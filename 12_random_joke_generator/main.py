import streamlit as st
import requests

def get_random_joke():
    try:
        # fetch a random joke from the api
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data =  response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        # Return fallback joke if exception occurs like internet issues
          return "Why did the programmer quit his job? \n because he didn't get array"
    
def main():
    """Main function to run the Streamlit app"""
    # set page title
    st.title("Random Joke Generator")
     # Add instruction text
    st.write("Click the button below to generate a random joke")

    # Create button and handle click
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)
        st.snow()
    
    # Add horizontal line
    st.divider()

    # Add footer
    # Footer using HTML, displaying text in the center
    st.markdown(
    """
    <div style="
    text-align: center; 
    background-color: #f9f9f9; 
    padding: 15px; 
    border-radius: 10px; 
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    font-family: Arial, sans-serif;
">
    <p style="font-size: 18px; font-weight: bold; color: #333; margin-bottom: 5px;">
        🤣 Joke from Official Joke API
    </p>
    <p style="font-size: 16px; color: #555;">
        Built by 
        <a href="https://github.com/sumair-khan21" 
           style="color: #007bff; text-decoration: none; font-weight: bold;">
            Sumair Khan
        </a> using Streamlit
    </p>
</div>

    """,
    unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
