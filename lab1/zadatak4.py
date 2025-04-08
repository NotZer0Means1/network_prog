import socket

def func():
    ip_addr = "8.8.8.8"
    host_name = socket.gethostbyaddr(ip_addr)
    print(f"Hostname: {host_name}")


if __name__ == '__main__':
    func()