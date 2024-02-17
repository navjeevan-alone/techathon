import os
import langchain
import transformers
from langchain.llms import GPT3, Textdavinci003  # Adjust based on your setup and preferences
from langchain.agents import TopicFinder, StyleAgent, NotesAgent, RelevantQuestionAgent, NextTopicAgent, RelevantTopicsAgent, QuizMakerAgent, ImageFinderAgent, MarkdownCreatorAgent

# Prompt input
prompt = input("Enter your learning prompt: ")

# Instantiate agents
topic_finder = TopicFinder()
style_agent = StyleAgent()
notes_agent = NotesAgent(api_key="AIzaSyBx7yebAjyzHHuEXbK9ihhgIIPgyH87HAQ")  # Replace with your API key
relevant_question_agent = RelevantQuestionAgent()
next_topic_agent = NextTopicAgent()
relevant_topics_agent = RelevantTopicsAgent()
quiz_maker_agent = QuizMakerAgent()
image_finder_agent = ImageFinderAgent()
markdown_creator_agent = MarkdownCreatorAgent()

# Initialize Langchain workflow
flow = langchain.new(start="prompt", end="markdown")

# Chain the agents together
flow.chain(    prompt, topic_finder, style_agent,
    topic_finder.topic, notes_agent, relevant_question_agent, next_topic_agent, relevant_topics_agent,
    style_agent.style, notes_agent.notes, relevant_question_agent.question, next_topic_agent.next_topic, relevant_topics_agent.relevant_topics,
    notes_agent.notes, next_topic_agent.next_topic, relevant_topics_agent.relevant_topics, quiz_maker_agent, image_finder_agent,
    quiz_maker_agent.quiz, image_finder_agent.images, markdown_creator_agent, notes_agent.notes, relevant_question_agent.question, next_topic_agent.next_topic, relevant_topics_agent.relevant_topics, 
)

 
# Get the final markdown string from the workflow
markdown_string = flow.run(prompt)

# Define filename and path
filename = "learning_about_magnets.md"  # Replace with your desired filename
path = os.path.join(os.getcwd(), filename)  # Save in current directory

# Open the file in write mode and write the markdown string
with open(path, "w") as f:
    f.write(markdown_string)

print(f"Markdown content saved to: {path}")
