import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = "AIzaSyBx7yebAjyzHHuEXbK9ihhgIIPgyH87HAQ"

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')
################################### SETUP DONE ###############################################

prompt = """
@YouTube  UserPrompt :"internal structure of electron"

  **Must contain the full video** (avoid linking to unavailable content)
  **Prioritize educational and high-quality sources** (e.g., universities, science channels)
  **Exclude videos with potential copyright violations** (focus on legitimate content)
  **Include video duration** (for informed selection)
  **Return up to 3 video links** (provide choices)

  **Optional enhancements:**
    - **Sort by relevance or view count** (refine results)
    - **Specify language preference** (cater to specific needs)
"""

response = model.generate_content(prompt)

to_markdown(response.text)

i = 0
with open(f"response_{i}.md", mode="w", encoding="utf-8") as resp_file:
#   video_link = get_video_link()
  resp_file.write(response.text)
