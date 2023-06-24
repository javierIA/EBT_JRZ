#!/usr/bin/env python3
"""Chat with GPT-3 from the Terminal."""
import os
import openai
if os.path.exists(os.path.expanduser(".openai")):
    openai.api_key = open(os.path.expanduser(".openai")).read().strip()
else:
    print("Enter your OpenAI API key: ", end="")
    openai.api_key = input()


starting_prompt = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."""
current_prompt = starting_prompt

def gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        stop=["\n"]
    )
    return response["choices"][0]["text"]
    
print("Welcome to GPT-3 Chat! Type 'quit' to exit, 'reset' to reset the conversation.")
print(current_prompt)
while True:
    print("Q: ", end="")
    user_input = input()
    if user_input == "quit":
        break
    if user_input == "reset":
        current_prompt = starting_prompt
        # clear screen
        print("\033c")
        print(current_prompt)
        continue
    current_prompt += f"\nQ: {user_input}\nA:"
    response = gpt3(current_prompt).strip()
    # add response without the newline
    print(f"A: {response}")
    current_prompt += f" {response}\n"
    print()