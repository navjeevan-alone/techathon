import requests
import json
# api_key = "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"


def create_prompt(topic):
    user_prompt = f"Return  JSON object only  Create a quiz on quiz_title  Format :( quiz_title: {topic}, quiz_id: random id with length 10 , questions: [ \(question: ,  options:Array of 4 options, correct_answer: str ), // create similar 5 question"
    return user_prompt


def generate_quiz(prompt):
    api_key = "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"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Adjust the model name as needed
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    quiz_data = response.json()
    if 'choices' not in quiz_data or len(quiz_data['choices']) == 0:
        print("No choices in response. Response might be an error or have unexpected format:", quiz_data)
        return None

    print("API Response:",quiz_data)
    # Extract the content from the response
    quiz_content_str = quiz_data['choices'][0]['message']['content'].strip()

    # Check if the content is not empty and is a valid JSON string
    if quiz_content_str:
        try:
            quiz_content_json = json.loads(quiz_content_str)
            # Save the quiz content as a properly formatted JSON file
            save_content_as_json(quiz_content_json)
            return quiz_content_json
        except json.JSONDecodeError:
            print("Error decoding JSON from content:", quiz_content_str)
            return None
    else:
        print("No content received from API.")
        return None


def save_content_as_json(content_json):
    with open('quiz_output.json', 'w') as json_file:
        json.dump(content_json, json_file, indent=4)


# Example usage
topic = "machine learning"
prompt = create_prompt(topic)
quiz_content_json = generate_quiz(prompt)
if quiz_content_json:
    save_content_as_json(quiz_content_json)
    print(quiz_content_json)
