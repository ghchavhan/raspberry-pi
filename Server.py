import socket
import sys

def main():
    HOST = ''
    PORT = 8888
        
    s = socket.socket()
    try:
        s.bind((HOST,PORT))
    except socket.error as msg:
        print ('Bind Failed.Error code:'+str(msg[0])+'Message:'+msg[1])
        sys.exit()
    print("Socket bind complete")
    
    s.listen(5)
    print("Socket know listening")
    
    while 1:
        conn,addr = s.accept()
        conn.send("Thanks for connecting".encode())
        print('Connect with ' + addr[0] + ' : ' + str(addr[1]))
    
if __name__ == '__main__':main()  