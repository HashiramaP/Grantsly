import os
from openai import OpenAI

client = OpenAI()

# Directory containing example HTML files
grants_ex_dir = "grants_ex"

# Read all HTML files from the directory
examples = []
for filename in os.listdir(grants_ex_dir):
    if filename.endswith(".html"):  # Ensure only HTML files are read
        with open(os.path.join(grants_ex_dir, filename), "r", encoding="utf-8") as file:
            examples.append({"role": "system", "content": f"Example from {filename}:\n{file.read()}"})

# Define the conversation with examples
messages = [
    {"role": "system", "content": "You work at a startup and your job is to fill up grant applications for your company."},
    *examples,  # Unpack the list of examples into the messages
    {
        "role": "user",
        "content": "What are the most common questions asked in grant applications?"
    }
]

# Send the request to OpenAI
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# Print the model's response
print(completion.choices[0].message.content)
