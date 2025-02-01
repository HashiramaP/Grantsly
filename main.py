import json
import os
from openai import OpenAI

client = OpenAI()

# Load the mock startup data from JSON
with open("mockScenario/mockStartup.json", "r", encoding="utf-8") as file:
    mock_startup_data = json.load(file)

# Convert JSON data into a readable format for OpenAI
startup_info = "\n".join([f"{key}: {value}" for key, value in mock_startup_data.items()])

# Start an interactive Q&A loop
print("Ask any question about the startup. Type 'exit' to quit.")
while True:
    user_question = input("You: ")
    if user_question.lower() == "exit":
        break
    
    messages = [
        {"role": "system", "content": "You are a representative of a startup. Answer questions based on the provided company information."},
        {"role": "system", "content": f"Here is the startup's information:\n{startup_info}"},
        {"role": "user", "content": user_question}
    ]
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    print("AI:", completion.choices[0].message.content)
