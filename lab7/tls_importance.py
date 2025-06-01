import socket
import ssl

def send_http_req(host, port, use_tls=False):
    req = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

    s = socket.create_connection((host, port), timeout=5)

    if use_tls:
        context = ssl.create_default_context()
        s = context.wrap_socket(s, server_hostname=host)

    s.sendall(req.encode())

    resp = b""
    while True:
        part = s.recv(4096)
        if not part:
            break
        resp += part

    s.close()
    return resp.decode(errors="ignore")


if __name__ == "__main__":
    host = "www.google.com"

    print("=" * 40)
    print("HTTP connection (port 80 - not protected):")
    print("=" * 40)
    resp_http = send_http_req(host, 80, use_tls=False)
    print(resp_http.split("\r\n\r\n")[0])

    print("\n" + "=" * 40)
    print("HTTPS connection (port 443 - TLS protected):")
    print("=" * 40)
    resp_https = send_http_req(host, 443, use_tls=True)
    print(resp_https.split("\r\n\r\n")[0])
