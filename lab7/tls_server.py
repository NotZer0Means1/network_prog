import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

def start_tls_echo_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print(f"[TLS SERVER] Waiting on {HOST}:{PORT}...")

        with context.wrap_socket(sock, server_side=True) as ssock:
            while True:
                conn, addr = ssock.accept()
                print(f"[TLS SERVER] Communicating with {addr}")
                data = conn.recv(1024)
                if data:
                    print(f"[TLS SERVER] Sent: {data.decode()}")
                    conn.sendall(data)
                conn.close()

if __name__ == '__main__':
    start_tls_echo_server()
