import streamlit as st
mydict = {"name": "name", "cheetan": "chetan"}


class StreamlitApp:
    def __init__(self):
        self.video_link = ""

        self.content = ""
        self.user_input = ""

    def set_video_link(self, link):
        self.video_link = link

    def set_content(self, content):
        self.content = content

    def set_user_input(self, input_value):
        self.user_input = input_value

    def render_layout(self):
        st.title("Design Dynamos")
        st.code("a=123")
        st.json(mydict)
        st.video(self.video_link)
        st.markdown(self.content)
        self.user_input = st.text_input("Enter your input")
        submit = st.button("Submit")
        if submit:
            self.handle_submit()

    def handle_submit(self):
        # You can define what happens when the submit button is clicked
        # For example, you might want to display the user input or use it in some way
        st.write(f"You submitted: {self.user_input}")


# Create an instance of the app
app = StreamlitApp()

# You can set the initial values for video, content, and input here
app.set_video_link('https://www.example.com/sample_video.mp4')
app.set_content('# type prompt to find youtube videos')

# Render the Streamlit layout
app.render_layout()
