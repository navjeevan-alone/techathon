import csv
import json
import requests
import time

API_KEY = "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"
CSV_FILE_PATH = "quiz_responses.csv"
ANALYSIS_FILE_PATH = "quiz_analysis.txt"


def send_request(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1000
    }
    response = requests.post(
        "https://api.openai.com/v1/completions", headers=headers, json=data)
    return response.json()


def take_quiz(quiz_json):
    correct_answers = 0
    with open(CSV_FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Options", "Selected Option",
                        "Correct Option", "Time Taken (seconds)"])

        for question in quiz_json.get("questions", []):
            print("\n" + question["question"])
            for idx, option in enumerate(question["options"], start=1):
                print(f"{idx}. {option}")

            start_time = time.time()
            selected_option = input("Your answer (number): ")
            end_time = time.time()

            selected_option_text = question["options"][int(selected_option)-1]
            time_taken = round(end_time - start_time, 2)
            writer.writerow([question["question"], question["options"],
                            selected_option_text, question["answer"], time_taken])

            if selected_option_text == question["answer"]:
                correct_answers += 1
                print("Correct!")
            else:
                print("Incorrect.")

    return correct_answers, len(quiz_json.get("questions", []))


def analyze_results():
    with open(CSV_FILE_PATH, "r") as file:
        csv_data = file.read()
    analysis_json = send_request(
        f"Analyze the following quiz responses:\n{csv_data}")
    analysis_text = analysis_json.get("choices", [{}])[0].get("text", "")
    with open(ANALYSIS_FILE_PATH, "w") as file:
        file.write(analysis_text)
    return analysis_text

def create_prompt(user_prompt,num):

    number_of_ques = 5
    prompt = """Return  JSON object only 
    Create a quiz on  magnets
    Format : {
    "quiz_title":{user_prompt},
    "quiz_id" : random id with length 10 ,
    "questions": [
        {
        "question": ,
        "options":Array of 4 options,
        "correct_answer": str 
        }, // create similar {number_of_ques} question 
    this i am using as string in python giving error
    convert above para to python string by using  escape character """

if __name__ == "__main__":
    user_prompt = input("Enter your quiz topic: ")
    request_prompt = create_prompt(user_prompt,5)
    quiz_json = send_request(request_prompt)
    correct_answers, total_questions = take_quiz(quiz_json)
    print(f"\nYour Score: {correct_answers}/{total_questions}")
    analysis_text = analyze_results()
    print("\nQuiz Analysis:")
    print(analysis_text)
