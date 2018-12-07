import json
from difflib import SequenceMatcher

#------------- EXTRACTING DATA AS PYTHON DICT FROM JSON -----------#
print("Basic English dictionary\n")
data = json.load(open("dictionary.json"))

#--------------------- SEARCH FOR WORD IN  DATA--------------------#
def search(word):
    return data[word]

#--------------- FUNCTION TO FIND SIMILAR WORD --------------------#
def similarity(word):
    listen=[]
    for i in data.keys():
        if SequenceMatcher(None, word, i).ratio()>=0.7:
            listen.append(i)
        else:
            continue
    return listen



#-------------- USER INTERACTION AND RESULT GENERATING-------------#

keyword=input("Please enter the word : ")
keyword=keyword.lower()

if keyword in data.keys():
    print(search(keyword))

#---------------- CHECKING SPELL MISTAKES FROM USER---------------#
else:
    while(keyword not in data.keys()):
        listen_n=similarity(keyword)
        print("\nCheck the spelling with these words: %s" %listen_n)
        keyword= input("\nEnter new word: ")
    print(search(keyword))
