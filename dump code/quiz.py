import streamlit as st

# Define quiz questions and answers
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"}
]

# Function to display a question and handle user's answer


def display_question(question_index):
    # Display the current question
    question = quiz_questions[question_index]["question"]
    answer = quiz_questions[question_index]["answer"]
    user_answer = st.text_input(question, "").strip()

    # Submit button for the current question
    if st.button("Submit"):
        if user_answer.lower() == answer.lower():
            st.success("That's correct!")
            st.session_state.score += 1
        else:
            st.error(
                f"Sorry, that's incorrect! The correct answer is {answer}.")

        # Move to the next question or show final score
        if question_index + 1 < len(quiz_questions):
            st.session_state.question_index += 1
        else:
            st.session_state.quiz_finished = True
            st.write(
                f"Quiz finished! Your final score is {st.session_state.score}/{len(quiz_questions)}.")


# Initialize session state variables
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

# Streamlit app layout and logic
st.title("Quiz App")

if not st.session_state.quiz_finished:
    display_question(st.session_state.question_index)
else:
    st.write(
        f"Quiz finished! Your final score is {st.session_state.score}/{len(quiz_questions)}.")
