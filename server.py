import socket
from parser import CommandParser
from store import Store
import threading


PORT=6380
HOST="127.0.0.1"
store = Store()
parser = CommandParser(store)


def client_handler(conn, addr):
    try:
        with conn:
            buffer = b""
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                buffer += data

                while b"\n" in buffer:
                    # split buffer only once, then assign first value to `line`
                    # and the rest to `buffer`. then it keeps going until there's no more \n in buffer
                    line, buffer = buffer.split(b"\n", 1)
                    command = line.decode('utf-8')
                    response = parser.execute(command)

                    conn.sendall((response + "\n").encode('utf-8'))
    except ConnectionResetError:
            print("Client disconnected")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        print(f"Client connected: {addr}")
        thread = threading.Thread(target=client_handler, args=(conn, addr))
        thread.start() # start a new thread for each client

        print(f"Active clients: {threading.active_count()}")
