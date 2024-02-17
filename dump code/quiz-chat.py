import csv
import json
import requests
import time

# Replace with your actual OpenAI API key
API_KEY = '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'
QUIZ_JSON_PATH = 'quiz_questions.json'
CSV_FILE_PATH = 'quiz_responses.csv'
ANALYSIS_JSON_PATH = 'quiz_analysis.json'
number_of_question = 5

def generate_quiz(prompt):
    headers = {'Authorization': 'Bearer {}'.format(API_KEY), 'Content-Type': 'application/json'}
    data = { 'model':"gpt-3.5-turbo-1106", 'response_format':{"type":"json_object"}, 'prompt': prompt, 'temperature': 0.7, 'max_tokens': 1000}
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions', headers=headers, json=data)
    quiz_json = response.json()
    with open(QUIZ_JSON_PATH, 'w') as f:
        json.dump(quiz_json, f)
    return quiz_json

def log_response(question_id, question, selected_option, correct_option, time_taken):
    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([question_id, question, selected_option, correct_option, time_taken])

def take_quiz():
    with open(QUIZ_JSON_PATH, 'r') as f:
        quiz_json = json.load(f)
    
    if not quiz_json.get('questions'):
        print("No questions found in the quiz.")
        return
    
    correct_count = 0
    for question in quiz_json['questions']:
        print("\nQuestion:", question.get('question'))
        options = question.get('options', [])
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        
        start_time = time.time()
        try:
            selected_idx = int(input("Your answer (number): ")) - 1
            selected_option = options[selected_idx] if 0 <= selected_idx < len(options) else "Invalid"
        except (ValueError, IndexError):
            selected_option = "Invalid"
        end_time = time.time()
        
        correct_option = question.get('answer')
        time_taken = round(end_time - start_time, 2)
        
        if selected_option == correct_option:
            correct_count += 1
            print("Correct!")
        else:
            print("Incorrect.")
        
        log_response(question.get('id'), question.get('question'), selected_option, correct_option, time_taken)

    print(f"\nYour score: {correct_count}/{len(quiz_json['questions'])}")


def analyze_responses():
    with open(CSV_FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        analysis = {
            'total_questions': 0,
            'correct_answers': 0,
            'average_time_per_question': 0
        }
        total_time = 0
        for row in reader:
            analysis['total_questions'] += 1
            if row[2] == row[3]:  # Selected option is correct
                analysis['correct_answers'] += 1
            total_time += float(row[4])
        analysis['average_time_per_question'] = total_time / \
            analysis['total_questions'] if analysis['total_questions'] else 0
    with open(ANALYSIS_JSON_PATH, 'w') as f:
        json.dump(analysis, f)
    print(f"Analysis saved to {ANALYSIS_JSON_PATH}")

if __name__ == '__main__':
    topic = input("Enter a topic for the quiz: ")
    user_prompt=f"Return  JSON object only  Create a quiz on quiz_title  Format :( quiz_title: {topic}, quiz_id: random id with length 10 , questions: [ \(question: ,  options:Array of 4 options, correct_answer: str ), // create similar 5 question"    
    
    generate_quiz(user_prompt)
    time.sleep(5)
    take_quiz()
    analyze_responses()
