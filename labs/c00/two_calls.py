import os
import anthropic

client = anthropic.Anthropic()   # finds ANTHROPIC_API_KEY in the environment by itself

response1 = client.messages.create(
    model=os.environ["AGENT_MODEL"],      # the model name you stored
    max_tokens=300,                       # the most it may write back
    messages=[
        {"role": "user", "content": "My name is Dylan"},
    ],
)

for block in response1.content:            # the reply is a list of blocks
    if block.type == "text":
        print(block.text)

response2 = client.messages.create(
    model=os.environ["AGENT_MODEL"],      # the model name you stored
    max_tokens=300,                       # the most it may write back
    messages=[
        {"role": "user", "content": "What is my name?"},
    ],
)

for block in response2.content:            # the reply is a list of blocks
    if block.type == "text":
        print(block.text)

print("call 1 input tokens:", response1.usage.input_tokens)
print("output tokens:", response1.usage.output_tokens)
print("call 2 input tokens:", response2.usage.input_tokens)
print("output tokens:", response2.usage.output_tokens)