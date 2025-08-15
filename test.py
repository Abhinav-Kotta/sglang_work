from sglang.test.doc_patch import launch_server_cmd
from sglang.utils import wait_for_server, print_highlight, terminate_process
import json

# Server 1
server1, port1 = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path qwen/qwen2.5-0.5b-instruct --host 0.0.0.0 --tp 2"
)
wait_for_server(f"http://localhost:{port1}")
print(f"Server 1 started on http://localhost:{port1}")

# Server 2
server2, port2 = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path mistralai/Mistral-7B-Instruct-v0.3 --host 0.0.0.0 --tp 2"
)
wait_for_server(f"http://localhost:{port2}")
print(f"Server 2 started on http://localhost:{port2}")

with open("ports.json", "w") as f:
    json.dump({"pserver_port1": port1, "server_port2": port2}, f)
