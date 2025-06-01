import socket
import sys

socket.setdefaulttimeout(0.5)

def port_check(ip_adresa, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_adresa, port))
        s.close()
        try:
            servis = socket.getservbyport(port)
        except OSError:
            servis = "Unknown servise"
        return (port, servis)
    except (socket.timeout, socket.error):
        return None

def scan_host(ip_adresa, pocetni_port, zavrsni_port):
    otvoreni_portovi = []
    print(f"Scanning {ip_adresa} from port {pocetni_port} to {zavrsni_port}...")
    for port in range(pocetni_port, zavrsni_port + 1):
        rezultat = port_check(ip_adresa, port)
        if rezultat:
            otvoreni_portovi.append(rezultat)
    return otvoreni_portovi

def validate_port(port):
    return 1 <= port <= 65535

if __name__ == "__main__":

    ip = sys.argv[1]

    try:
        first = int(sys.argv[2])
        last = int(sys.argv[3])
    except ValueError:
        print("Ports have to be digits.")
        sys.exit(1)

    if not (validate_port(first) and validate_port(last)) or first > last:
        print("Wrong range of ports. You need tpo use 1–65535.")
        sys.exit(1)

    otvoreni = scan_host(ip, first, last)

    if otvoreni:
        print(f"\nOpen ports on {ip}:")
        for port, servis in otvoreni:
            print(f"- {port} ({servis.upper()})")
    else:
        print(f"\nThere are no open ports on {ip} in given range.")
