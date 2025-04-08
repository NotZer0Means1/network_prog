import socket
import subprocess

def is_host_reachable(domain):
    try:
        response = subprocess.run(["ping", "-c", "1", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if response.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Greska pri pinganju: {e}")
        return False


def print_machine_info():
    domain_name = "google.com"
    flag = is_host_reachable(domain_name)
    if(flag):
        ip_address = socket.gethostbyname(domain_name)
        print("ip_address of %s: %s" % (domain_name, ip_address))
    else:
        print("Domain is not reachable")

if __name__ == '__main__':
    print_machine_info()