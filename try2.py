import textwrap
from IPython.display import Markdown 

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import json
data={}
# Open the JSON file for reading
with open('response.json', 'r') as file:
    # Parse the JSON file into a Python dictionary
    data = json.load(file)
print(data)
with open(f"response_2.md", mode="w", encoding="utf-8") as resp_file:
    resp_file.write(data["notes"])
