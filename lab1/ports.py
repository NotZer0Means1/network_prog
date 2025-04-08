import subprocess
import socket

def get_ports_from_netstat():
    try:
        command = ["netstat", "-a"]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return []

        ports = []

        lines = result.stdout.splitlines()

        for line in lines:
            if "LISTEN" in line:
                parts = line.split()

                local_address = parts[3]

                local_port = local_address.split(":")[-1]

                ports.append(int(local_port))

        return ports

    except Exception as e:
        print(f"Error during execution: {e}")
        return []

def get_service_by_port(port):
    try:
        service_name = socket.getservbyport(port, proto='tcp')
        return service_name
    except OSError:
        return None

ports = get_ports_from_netstat()
if ports:
    print("Listening ports and their services:")
    for port in ports:
        service = get_service_by_port(port)
        if service:
            print(f"Port {port} is used by {service}")
        else:
            print(f"Port {port} has no associated service.")
else:
    print("No listening ports found or error occurred.")
