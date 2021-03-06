import time
from datetime import datetime as dt


hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = r"hosts"
redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours")
        with open(hosts_path, "r+") as hosts:
            content = hosts.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hosts.write(redirect+" "+website+"\n")


    else:
        print("Fun Hours")
        with open(hosts_path, "r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hosts.write(line)
            hosts.truncate()
    time.sleep(5)
