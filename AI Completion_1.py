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

# Send a request to the chat completion endpoint with properly formatted messages
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "I'm using an API key to get a response from ChatGPT inside of Visual Studio Code. Are your responses being generated within VS Code or on OpenAI's end and then sent to my terminal?"
        }
    ]
)

# Print the chat completion's response text
print(response.choices[0].message.content)

