import time
import textwrap
import os
import google.generativeai as genai
from IPython.display import display, Markdown
from dotenv import load_dotenv

load_dotenv()

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def gemini_model(text):
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    start_time = time.time()
    response = model.generate_content(text, stream=True)
    end_time = time.time()

    for chunk in response:
        for char in chunk.text:
            print(char, end='', flush=True)
            time.sleep(0.03)
        print("\n" + "_" * 80)

    elapsed_time = end_time - start_time
    print(f"Response time: {elapsed_time:.2f} seconds")

def user_input():
    while True:
        user_input = input("What is your question? (Enter 'exit' to quit) ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        gemini_model(user_input)

def main():
    user_input()

if __name__ == "__main__":
    main()
