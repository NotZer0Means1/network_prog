import socket
print("Unesite port. Za kraj unosa upisi -1")
ports = []
while(True):
    port = int(input())
    if port == -1:
        break
    ports.append(port)


for port in ports:
    print(f"Port {port}: {socket.getservbyport(port)}")