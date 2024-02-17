import os
from openai import OpenAI

api_key = "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"


client = OpenAI(api_key=api_key)


def generate_mcq(topic):


    


    prompt = f"Generate a multiple choice question on the topic of {topic}. Include four possible answers, with one correct answer and three distractors. Indicate the correct answer with (correct)."
    

    parameters = {
        "model": "gpt-3.5-turbo-instruct",  # You can choose different models
        "temperature": 0.7,
        "max_tokens": 150,
    }
    
    # Send the request to the API
    response = client.completions.create(prompt=prompt, **parameters, n=1, stop=None)

    # response = client.completions.create(engine="text-davinci-003",  # Adjust engine as needed
    # prompt=prompt,
    # max_tokens=150,  # Adjust maximum tokens as needed
    # n=1,
    # stop=None,
    # temperature=0.7  # Adjust temperature for creativity
    # )

    question_and_answers = response.choices[0].text.strip().split(";")
    return question_and_answers


topic = "machine learning"  # Replace with your desired topic
mcq = generate_mcq(topic)
print(mcq)
