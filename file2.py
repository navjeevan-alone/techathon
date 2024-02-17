import requests
import json


def generate_quiz(topic):
    # Replace with your actual OpenAI API key
    api_key = "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"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Adjust the model name as needed
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Create a quiz about {topic}."}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    quiz_data = response.json()

    # Check for the 'choices' key in the response
    if 'choices' not in quiz_data or len(quiz_data['choices']) == 0:
        print("No choices in response. Response might be an error or have unexpected format:", quiz_data)
        return None

    # Check for the 'message' key within the first choice
    if 'message' not in quiz_data['choices'][0]:
        print("No message in the first choice. Response might be an error or have unexpected format:",
              quiz_data['choices'][0])
        return None

    quiz_content_str = quiz_data['choices'][0]['message']['content'].strip()

    if quiz_content_str:
        try:
            quiz_content_json = json.loads(quiz_content_str)
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
topic = "magnets"
quiz_content_json = generate_quiz(topic)
if quiz_content_json:
    print(quiz_content_json)
