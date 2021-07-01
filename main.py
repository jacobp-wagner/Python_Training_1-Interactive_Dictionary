import json

# used to provide delta values when user inputs a word not found in dictionary
from difflib import get_close_matches
dictionary = json.load(open("App1_InteractiveDictionary/Files/data.json"))


# function will search dictionary "dictionary" for key value entered by user
def definition(w):
    # updating variable to account for different case from user input
    w = w.lower()
    # checks for word as all lowercase
    if w in dictionary:
        return dictionary[w]
    # checks for proper nouns such as city names i.e. "Paris"
    elif w.capitalize() in dictionary:
        return dictionary[w.capitalize()]
    # checks for acronyms i.e. USA
    elif w.upper() in dictionary:
        return dictionary[w.upper()]
    # determine if there are any alternate suggestions
    elif len(get_close_matches(w, dictionary.keys(), n=1, cutoff=0.75)) > 0:
        # finds closest match in "dictionary" keys to user input "w" by delta score calculated by
        suggest = get_close_matches(w, dictionary.keys(), n=1)[0]
        accept = input("Word not found. Did you mean {} (Y/N)".format(suggest))
        # updating variable to account for different case from user input
        accept = accept.lower()
        if accept == "y":
            return dictionary[suggest]
        elif accept == "n":
            return "No definition found!"
        else:
            return "Invalid entry!"
    else:
        return "Word not found. No suggestions available."


word = input("Enter a word to search: ")

output = definition(word)

# format "output" to display one definition per line when a list type, or just print when a string type
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
