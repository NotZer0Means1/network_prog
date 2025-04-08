import socket
HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CLIENT] Connected to server.")
    while True:
        message = input("Unesi poruku (ili 'exit'): ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"[CLIENT] Received: {data.decode()}")