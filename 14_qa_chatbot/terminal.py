import google.generativeai as genai
import os
from dotenv import load_dotenv


# load the environment variables
load_dotenv()

# initialize the gemini api key
# configure ka kam ye hy k google ka api key load ho jaye
# aur hum use karenge ai k liye
# getenv ka kam ye hy k env file main se api key load ho jaye
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_input = input("\nEnter your question (or 'exit' to quit): ")
    if user_input.lower() == "quit":
        print("Thank you for using the chatbot!")
        break
    


    response = model.generate_content(user_input)

    print("\nResponse:", response.text)