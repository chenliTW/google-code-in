import socket
import paramiko
import threading
import time

HOST = "127.0.0.1"
PORT = 2200

host_key = paramiko.RSAKey(filename="RSA.key")

log = open("log.txt","a+")

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        log.write(username+" - "+password+"\n")
        log.flush();
        return paramiko.AUTH_SUCCESSFUL

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(100)
    while True:
        client, addr = sock.accept()
        log.write(time.strftime("[%Y-%m-%d %H:%M:%S] - ", time.localtime())+addr[0]+" - ")
        try:
            tran = paramiko.Transport(client)
            tran.set_gss_host(socket.getfqdn(""))
            tran.load_server_moduli()
            tran.add_server_key(host_key)
            server = Server()
            tran.start_server(server=server)
            chan = tran.accept(None)
            server.event.wait(10)
            chan.send("Welcome to the server!\r\n")
            while True:
                chan.send("sh-5.0$ ")
                recv=chan.makefile("rU").readline().strip("\r\n")
                if recv=="exit":
                    break
                if len(recv):
                    chan.send("\r\nsh: "+recv+" : command not found\r\n")
                else:
                    chan.send("\r\n")
            chan.send("\r\nlogout\r\n")
            chan.close()
        except Exception as e:
            print(str(e.__class__))
main()