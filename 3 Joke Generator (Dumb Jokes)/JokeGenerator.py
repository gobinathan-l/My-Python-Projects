import requests
from random import choice
import pyfiglet

header=pyfiglet.figlet_format("Dumb Jokes,")
print(header)
url         =   "https://icanhazdadjoke.com/search"
input_term  =   input("What would you like to search for? : ")
response    =   requests.get(url, headers={"Accept":"application/json"}, params={"term":input_term} ).json()
total_jokes =   response['total_jokes']

if total_jokes > 1:
    print(f"I found {total_jokes} Jokes about {input_term}, Here's one.")
    results = response['results']
    print(choice(results)['joke'])
elif total_jokes == 1:
    print("Here's your Joke,")
    print(response['results'][0]['joke'])
else:
    print(f"No Jokes found for your Query '{input_term}'.")
