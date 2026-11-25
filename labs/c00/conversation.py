import os
import anthropic

client = anthropic.Anthropic()   # finds ANTHROPIC_API_KEY in the environment by itself

response = client.messages.create(
    model=os.environ["AGENT_MODEL"],      # the model name you stored
    max_tokens=300,                       # the most it may write back
    messages=[
        {"role": "user", "content": "My name is Dylan"},
	{"role": "assistant", "content": "Hi Dylan, nice to meet you! How can I help you today?"},
	{"role": "user", "content": "What is my name?"},

    ],
)

for block in response.content:            # the reply is a list of blocks
    if block.type == "text":
        print(block.text)

print("input tokens:", response.usage.input_tokens)
print("output tokens:", response.usage.output_tokens)