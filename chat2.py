import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
GOOGLE_API_KEY = "AIzaSyBx7yebAjyzHHuEXbK9ihhgIIPgyH87HAQ"

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

def create_prompt(user_prompt):
  prompt = """@Youtube 
  UserPrompt : {user_prompt}
  Find the most suitable video on given topic and return link
  """
  return prompt


user_prompt = "what is quamtum computing"


def get_video_link():
  final_prompt = create_prompt(user_prompt)
  # calling llm here
  response = model.generate_content(final_prompt)
  return response.text


i = 0
with open(f"response_{i}.md", mode="w", encoding="utf-8") as resp_file:
  i += 1
  video_link = get_video_link()
  resp_file.write(video_link)
