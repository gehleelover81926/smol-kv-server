import socket
from parser import CommandParser
from store import Store

PORT=6380
HOST="127.0.0.1"
store = Store()
parser = CommandParser(store)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        with conn:
            print(f"Client connected: {addr}")
            buffer = b""

            while True:
                data = conn.recv(1024)

                if not data:
                    break

                print(data)

                buffer += data
                response = "";
                while (b"\n" in buffer):
                    # split buffer only once, then assign first value to `line`
                    # and the rest to `buffer`. then it keeps going until there's no more \n in buffer
                    line, buffer = buffer.split(b"\n", 1)

                    command = line.decode('utf-8')
                    response = parser.execute(command)


                conn.sendall((response +"\n").encode("utf-8`")) # sockets communicates in bytes so we need to encode the response to utf-8
