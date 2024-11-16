import subprocess

def list_ports_windows():
    result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
    print(result.stdout)

list_ports_windows()
