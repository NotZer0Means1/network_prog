import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

def start_tls_client(poruka):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations('server.crt')

    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            print(f"[TLS CLIENT] Communicating with {HOST}:{PORT}")
            print("[TLS CLIENT] Certificate is valid!.")
            ssock.sendall(poruka.encode())
            odgovor = ssock.recv(1024)
            print(f"[TLS CLIENT] Response: {odgovor.decode()}")

if __name__ == '__main__':
    start_tls_client("Hello, we connceted with tls!")
