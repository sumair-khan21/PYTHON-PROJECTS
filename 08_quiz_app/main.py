import streamlit as st
import random
import time

st.title("Python Quiz App")

questions = [
    {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def",
    },
    {
        "question": "Which data type is used to store multiple values in a single variable?",
        "options": ["int", "str", "list", "bool"],
        "answer": "list",
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#",
    },
    {
        "question": "Which function is used to get user input in Python?",
        "options": ["input()", "scan()", "get()", "read()"],
        "answer": "input()",
    },
    {
        "question": "What will `type(10)` return?",
        "options": ["str", "float", "int", "bool"],
        "answer": "int",
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["tuple", "int", "list", "str"],
        "answer": "list",
    },
    {
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["5", "6", "8", "9"],
        "answer": "8",
    },
    {
        "question": "Which loop is used when the number of iterations is not known beforehand?",
        "options": ["for loop", "while loop", "do-while loop", "repeat loop"],
        "answer": "while loop",
    },
    {
        "question": "Which method is used to remove the last item from a list?",
        "options": ["delete()", "remove()", "pop()", "discard()"],
        "answer": "pop()",
    },
    {
        "question": "Which keyword is used to exit a loop prematurely?",
        "options": ["exit", "break", "continue", "stop"],
        "answer": "break",
    },
    {
        "question": "What is the default return type of input() function?",
        "options": ["int", "str", "bool", "float"],
        "answer": "str",
    },
    {
        "question": "Which built-in function is used to convert a string into an integer?",
        "options": ["str()", "int()", "float()", "bool()"],
        "answer": "int()",
    },
    {
        "question": "How do you start a multi-line comment in Python?",
        "options": ["/* */", "#", '""" """', "//"],
        "answer": '""" """',
    },
    {
        "question": "Which operator is used for floor division in Python?",
        "options": ["/", "//", "%", "**"],
        "answer": "//",
    },
    {
        "question": "Which function is used to find the length of a list?",
        "options": ["length()", "size()", "count()", "len()"],
        "answer": "len()",
    },
    {
        "question": "How do you declare a variable in Python?",
        "options": ["var x = 10", "x = 10", "int x = 10", "declare x = 10"],
        "answer": "x = 10",
    },
    {
        "question": "Which of the following is NOT a valid variable name in Python?",
        "options": ["my_var", "_var", "2var", "var2"],
        "answer": "2var",
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "try", "except", "finally"],
        "answer": "try",
    },
    {
        "question": "Which function is used to open a file in Python?",
        "options": ["open()", "read()", "write()", "load()"],
        "answer": "open()",
    },
    {
        "question": "Which module is used for working with random numbers in Python?",
        "options": ["math", "random", "rand", "numbers"],
        "answer": "random",
    },
]


# Streamlit session state ko use karke current question store kar rahe hain
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)  # Random question select kar rahe hain

question = st.session_state.current_question  # Current question ko ek variable me store kar rahe hain

st.subheader(question["question"])  # Question ko display kar rahe hain Streamlit ke UI me

# Streamlit ka radio button, jo user ko answer choose karne ki option deta hai
select_options = st.radio("Choose your answer", question["options"], key="answer")

# Streamlit ka button jo answer submit karega
if st.button("Submit Answer"):
    # Agar user ka selected answer correct hai
    if select_options == question["answer"]:
        st.success("Correct Answer!")  # Success message show karega
        st.balloons()  # Balloons animation show karega
    else:
        st.error("Incorrect! The correct answer is " + question["answer"])  # Galat answer par error message show karega

    time.sleep(5)  # 5 second ka delay daal rahe hain, taake user answer dekh sake

    # Next question randomly select kar rahe hain
    st.session_state.current_question = random.choice(questions)

    st.rerun()  # Page ko dubara reload kar rahe hain taake naya question aaye