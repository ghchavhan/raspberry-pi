import socket

def main():
    s = socket.socket()
    host = socket.gethostname()
    port = 8888
    s.connect((host,port))
    print("Reply from server: ",s.recv(1024).decode())
    s.close
if __name__ == '__main__': main()