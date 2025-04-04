import streamlit as st


def main():
    
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation")

    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter First Number", value=0.0)
    
    with col2:
        num2 = st.number_input("Enter Second Number", value=0.0)    

    operations = st.selectbox(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
    )
    
    if st.button("Calculate"):
        try:
            if operations == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operations == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operations == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            else:
                if num2 == 0:
                    st.error("Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"
            st.success(f"{num1} {symbol} {num2} = {result}")
            # exception means object in python 
            # is puri condition ko shortcut name de dia e
        except Exception as e:
            # str is the of python ye string m error show karega number bhi likh sakhte hain
            st.error(f"An error occurred: {str(e)}")
            
# jb bhi ye main ki file run hogi toh sb se phle main ka function run hoga
# yaha python k interpretuer ko bata rahe hain k phle main.py ko run krna hy
if __name__ == "__main__":
    main()
