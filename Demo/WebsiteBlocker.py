import time
from datetime import datetime as dt

hosts_path=r"hosts"
website_list=["facebook.com","www.facebook.com"]
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(hosts_path,"r+") as hosts:
            content = hosts.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hosts.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,"r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hosts.write(line)
            hosts.truncate()

    time.sleep(5)
