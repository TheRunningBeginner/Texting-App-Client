import socket


class Client:
    def __init__(self, username, server, port):
        self.OPERATION_HEADER = 2
        self.USER_NAME_LENGTH_HEADER = 2
        self.STATUS_CODE_HEADER = 3
        self.IP_HEADER = 2

        self.PORT = port
        self.FORMAT = 'utf-8'
        self.SERVER = server
        self.ADDR = (self.SERVER, self.PORT)

        self.user_name = username

        self.client = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def disconnect(self):
        self.client.close()

    def send_user_name(self, requested_user_name=""):
        user_name_to_send = self.user_name

        if requested_user_name != "":
            user_name_to_send = requested_user_name

        self.client.send(str(len(user_name_to_send)).zfill(self.USER_NAME_LENGTH_HEADER).encode(self.FORMAT))
        self.client.send(user_name_to_send.encode(self.FORMAT))

    def send_operation(self, operation):
        self.client.send(operation.encode(self.FORMAT))

    def recv(self, length):
        return self.client.recv(length).decode(self.FORMAT)

    def send_online(self):
        self.connect()

        self.send_operation("on")
        self.send_user_name()

        print(self.recv(self.STATUS_CODE_HEADER))

        self.disconnect()

    def send_alive(self):
        self.connect()

        self.send_operation("al")
        self.send_user_name()

        self.disconnect()

    def get_ip(self, requested_user_name):
        self.connect()

        self.send_operation("ip")
        self.send_user_name()
        self.send_user_name(requested_user_name)

        ip_length = self.recv(self.IP_HEADER)
        ip = self.recv(int(ip_length))

        self.disconnect()

        return ip
