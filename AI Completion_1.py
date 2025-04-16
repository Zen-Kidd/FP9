import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables explicitly from the .env file
load_dotenv()

# Get API key from environment variable
apikey = os.getenv("OPENAI_API_KEY")

# Raise error if the API key is not found
if not apikey:
    raise ValueError("API key not found. Check your .env file and ensure it is in the proper location and formatted correctly.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=apikey)

def submit_prompt():
    # Get the user's prompt from the input text box
    prompt = prompt_text.get("1.0", tk.END).strip()
    if not prompt:
        return  # do nothing if prompt is empty

    try:
        # Send a request to the chat completions endpoint with the prompt as a user message
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        # Extract the answer from the response
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"Error: {e}"

    # Update the output box with the response
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, answer)
    output_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("ChatGPT API GUI")

# Create a label and text box for the prompt input
tk.Label(root, text="Enter your prompt:").pack(pady=(10, 0))
prompt_text = tk.Text(root, wrap=tk.WORD, height=10, width=60)
prompt_text.pack(padx=10, pady=10)

# Create a submit button that calls the submit_prompt function
submit_btn = tk.Button(root, text="Submit", command=submit_prompt)
submit_btn.pack(pady=(0, 10))

# Create a label and a scrolled text widget for displaying the response
tk.Label(root, text="Response:").pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=60)
output_text.pack(padx=10, pady=(0, 10))
output_text.config(state=tk.DISABLED)

# Start the Tkinter event loop
root.mainloop()
