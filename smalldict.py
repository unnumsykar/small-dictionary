import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        new = input("Did you mean %s instead. Type y if yes or n if no:" % get_close_matches(w,data.keys())[0])    
        new = new.lower()
        if new == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif new == 'n':
            return "Sorry we couldn't find the word you entered"
        else:
            return "Type y/n not anything else." 
    else:
        return "The word entered is wrong, recheck and type again."


enter = input("Enter your word:")
means = meaning(enter)
print(means)
