#Time Based Website Blocker made by gobinathan-l
import time
from datetime import datetime as dt


hosts_path = r"C:\Windows\System32\drivers\etc\hosts" # The websites are rendered unavailable by redirecting them to localhost. Make sure you have no services running on localhost.
hosts_temp = r"hosts"
redirect = "127.0.0.1" # Localhost IP
website_list = ["facebook.com", "www.facebook.com"] # New websites can be added to this list

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,13): # To compare the Current Time with working Hours
        with open(hosts_temp, "r+") as hosts:
            content = hosts.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hosts.write(redirect+" "+website+"\n")


    else:
        with open(hosts_temp, "r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hosts.write(line)
            hosts.truncate()
    time.sleep(5)
