from dotenv import load_dotenv

import os
import openai
import json
import textExtractorFromPdf

# Load the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.environ['OPEN_AI_KEY']

# Create a prompt for GPT
prompt = """
Given a raw content extracted from a resume. Parse this raw content into json.

{text}
"""

# Send the prompt to GPT and get the response
textFromResume = textExtractorFromPdf.readTextFromPdf()
response = openai.Completion.create(model = "gpt-3.5-turbo-instruct", temperature = 0.9, prompt=prompt.format(text=textFromResume), max_tokens=2000)

# Extract the JSON from the response
json_data = response.choices[0].text

with open("parsed_resume.json", "w") as f:
  # Dump the parsed JSON resume to the file
  f.write(json_data)

# Print the JSON
print("resume parsed")
