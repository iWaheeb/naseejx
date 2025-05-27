import socket



def create_server(ip:str, port: int):
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    listen_sock.bind((ip, port))
    listen_sock.listen()
    while True:
        conn, addr = listen_sock.accept()
        print(f"{addr} connected")
        request = conn.recv(1024)
        print(request)
        CRLF = "\r\n"
        response = f"HTTP/1.0 200 OK{CRLF+CRLF}"
        conn.send(response.encode())
        print("end")
        conn.close()
