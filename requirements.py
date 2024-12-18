import subprocess

installation = subprocess.run(["pip3", "install", "discord"], capture_output=True)
print("dependencies installed (:")
