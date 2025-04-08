import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 9999))

server_socket.listen(1)
print("Server je pokrenut na portu 9999...")


client_socket, client_address = server_socket.accept()
print(f"Povezan sa klijentom: {client_address}")

client_socket.close()
server_socket.close()
