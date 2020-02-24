import json
from difflib import get_close_matches

data = json.load(open("data.json"))

#search dictionary funtion
def searchdic(wrd):
    wrd = wrd.lower()

#Is the word listed in the dictionary? 
    if wrd in data:
        return data[wrd]
#Compare words with similar spelling
    elif len(get_close_matches(wrd, data.keys())) > 0:
        confirm_yn = input("Did you mean \"%s\" instead? \ny/n?: " % get_close_matches(wrd, data.keys())[0])
        if confirm_yn == "y":
            return data[get_close_matches(wrd, data.keys())[0]]
        elif confirm_yn == "n":
            return "The word doesn't exist."
        else:
            return "We didn't understand..."
    else:
        return "The word does not exist. Please double check it"


word = input("Type word to search definition: ")

output = searchdic(word)

#Check if output is list or string
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)