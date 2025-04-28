import socket
from local_machine_info import print_machine_info
print_machine_info()

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("[UDP CLIENT] Type messages. Type 'exit' to quit.")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        s.sendto(message.encode(), (HOST, PORT))
        data, _ = s.recvfrom(1024)
        print(f"[UDP CLIENT] Server replied: {data.decode()}")