import selectors
import socket
import threading
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    handlers=[
        logging.FileHandler("server.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

sel = selectors.DefaultSelector()
clients = {}

HOST = 'localhost'
PORT = 65433

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ)

logging.info(f"CHAT SERVER started on {HOST}:{PORT}")

def log_active_users():
    while True:
        logging.info(f"Aktivnih korisnika: {len(clients)}")
        time.sleep(10)

threading.Thread(target=log_active_users, daemon=True).start()

while True:
    events = sel.select()
    for key, _ in events:
        if key.fileobj == lsock:
            conn, addr = lsock.accept()
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ)
            clients[conn] = {"addr": addr, "name": None}
        else:
            conn = key.fileobj
            try:
                data = conn.recv(1024)
                if data:
                    message = data.decode().strip()
                    if clients[conn]["name"] is None:
                        clients[conn]["name"] = message
                        logging.info(f"LOGIN: {clients[conn]['name']} from {clients[conn]['addr']}")
                    else:
                        if message == "/users":
                            user_list = [info["name"] for info in clients.values() if info["name"]]
                            response = "[SERVER] Aktivni korisnici:\n" + "\n".join(user_list) + "\n"
                            conn.sendall(response.encode())
                        else:
                            msg = f"{clients[conn]['name']}: {message}"
                            logging.info(msg)
                            for c in clients:
                                if c != conn:
                                    try:
                                        c.sendall(msg.encode())
                                    except Exception as e:
                                        logging.warning(f"Ne mogu da pošaljem poruku {clients[c]['name']}: {e}")
                else:
                    raise ConnectionResetError
            except Exception:
                name = clients[conn]["name"]
                logging.info(f"LOGOUT: {name if name else conn}")
                sel.unregister(conn)
                conn.close()
                del clients[conn]
