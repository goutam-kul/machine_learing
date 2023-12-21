import os 
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import streamlit as st

# GREETING_MESSAGE = "Hello, I am a chatbot. How can I help you today?"
# GOODBYE_MESSAGE = "Goodbye. It was nice talking to you."
# DEFAULT_RESPONSE = "I'm sorry, I don't understand."

    
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.environ['GOOGLE_API_KEY'] = 'AIzaSyDmBhzTawK-FHzCt5fb0qDjOKNdSps4f-c'
genai.configure(api_key='AIzaSyDmBhzTawK-FHzCt5fb0qDjOKNdSps4f-c')
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
    

model = genai.GenerativeModel('gemini-pro')
print('Hello, how can i help you today?')
while True:
    user_input  = input('\n-')
    response = model.generate_content(user_input)

    to_markdown(response.text)
    print(response.text)
    
    if user_input == 'Exit':
      print("Goodbye. It was nice talking to you.")
      break