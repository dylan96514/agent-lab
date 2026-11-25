import os
import anthropic

client = anthropic.Anthropic()   # finds ANTHROPIC_API_KEY in the environment by itself

response = client.messages.create(
    model=os.environ["AGENT_MODEL"],      # the model name you stored
    max_tokens=300,                       # the most it may write back
    system="Answer like a pirate.",
    messages=[
        {"role": "user", "content": "Say hello and tell me one fact about Seoul."},
    ],
)

for block in response.content:            # the reply is a list of blocks
    if block.type == "text":
        print(block.text)

print("input tokens:", response.usage.input_tokens)
print("output tokens:", response.usage.output_tokens)
print("stop reason:", response.stop_reason)
