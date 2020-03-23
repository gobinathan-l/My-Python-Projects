import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getValues(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        choice = input("Did you mean % s instead? Press Y for Yes and N for No: " % get_close_matches(w,data.keys())[0])
        if choice == "Y" or choice == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif choice == "N" or choice == "n":
            return "No Matches."
        else:
            return "Can't Understand your Query"
    else:
        return "No matches in our Database."


word = input("Enter your Word: ")

output = getValues(word)

if type(output) == list:
    c = 1
    for i in output:
        print(str(c) + ". "+ i)
        c+=c
else:
    print(output)
