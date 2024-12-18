import subprocess

installation = subprocess.run(["pip3", "install", "scapy"], capture_output=True)
print("dependencies installed (:")
