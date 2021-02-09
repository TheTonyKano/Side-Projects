word = input("Word you want to find: ").lower()
string = input("Enter string of letters: ").lower()

def pos(word, string):
    lstValue = []
    lstWord = sorted(word)
    for i in range(0, len(lstWord)):
        value = string.find(lstWord[i])
        if value >= 0:
            lstValue.append("Yes")
        else:
            lstValue.append("No")
    if "No" in lstValue:
        print("No")
    else: 
        print("Yes")
        
pos(word, string)