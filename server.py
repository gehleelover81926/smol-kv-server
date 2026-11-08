import socket

PORT=6380
HOST="127.0.0.1"

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

                while (b"\n" in buffer):
                    # split buffer only once, then assign first value to `line`
                    # and the rest to `buffer`. then it keeps going until there's no more \n in buffer
                    line, buffer = buffer.split(b"\n", 1)

                    print(line)
                    print(buffer)

                conn.sendall(data)
