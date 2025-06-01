import ssl
import socket

def get_certificate(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
            cert = secure_sock.getpeercert()
            return cert

if __name__ == "__main__":
    hostname = "www.google.com"
    certifikat = get_certificate(hostname)

    if certifikat:
        print(f"Certificate for {hostname}:\n")
        subject = dict(x[0] for x in certifikat['subject'])
        issuer = dict(x[0] for x in certifikat['issuer'])

        print("Subject:", subject)
        print("Issuer:", issuer)
        print("Valid from:", certifikat.get('notBefore'))
        print("Valid until:", certifikat.get('notAfter'))
    else:
        print("Impossiple to get certificate.")
