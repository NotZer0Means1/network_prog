import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.datetime.now())

HOST = '0.0.0.0'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                message = data.decode().strip()
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{time}] Poruka od {addr[0]}: {message}")

                if message == "Vladimir_Shevalev":
                    response = "Unos nije podrzan"
                else:
                    response = message

                conn.sendall(response.encode())
