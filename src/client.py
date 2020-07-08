import socket

OPERATION_HEADER = 2
USER_NAME_LENGTH_HEADER = 2
STATUS_CODE_HEADER = 3
IP_HEADER = 2


PORT = 5050
FORMAT = 'utf-8'
SERVER = ""
ADDR = (SERVER, PORT)

user_name = ""

client = None


def connect():
    global client

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)


def disconnect():
    client.close()


def send_user_name(requested_user_name=""):
    user_name_to_send = user_name

    if requested_user_name != "":
        user_name_to_send = requested_user_name

    client.send(str(len(user_name_to_send)).zfill(USER_NAME_LENGTH_HEADER).encode(FORMAT))
    client.send(user_name_to_send.encode(FORMAT))


def send_operation(operation):
    client.send(operation.encode(FORMAT))


def recv(length):
    return client.recv(length).decode(FORMAT)


def send_online():
    connect()

    send_operation("on")
    send_user_name()

    print(recv(STATUS_CODE_HEADER))

    disconnect()


def send_alive():
    connect()

    send_operation("al")
    send_user_name()

    disconnect()


def get_ip(requested_user_name):
    connect()

    send_operation("ip")
    send_user_name()
    send_user_name(requested_user_name)

    ip_length = recv(IP_HEADER)
    ip = recv(int(ip_length))

    disconnect()

    return ip
