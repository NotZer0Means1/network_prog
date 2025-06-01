import socket
import sys

socket.setdefaulttimeout(0.5)

def port_check(ip_adresa, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_adresa, port))
        print(f"Port {port} on {ip_adresa} is open.")
        s.close()
    except (socket.timeout, socket.error):
        print(f"Port {port} on {ip_adresa} is closed or unavailable.")

if __name__ == "__main__":
    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        print("Port have to be a number.")
        sys.exit(1)

    port_check(ip, port)
