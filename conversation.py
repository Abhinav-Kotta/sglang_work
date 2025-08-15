from sglang.utils import wait_for_server, print_highlight, terminate_process
import openai
import json

with open("ports.json", "r") as f:
    ports = json.load(f)

port1 = ports["pserver_port1"]
client = openai.Client(base_url=f"http://127.0.0.1:{port1}/v1", api_key="None")

response = client.chat.completions.create(
    model="qwen/qwen2.5-0.5b-instruct",
    messages=[
        {"role": "user", "content": "List 3 countries and their capitals."},
    ],
    temperature=0,
    max_tokens=64,
)

print_highlight(f"Response: {response}")