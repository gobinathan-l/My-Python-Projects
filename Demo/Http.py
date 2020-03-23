import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept":"application/json"})
content = response.json()

print(content['joke'])
print(f"Status: {content['status']}")
