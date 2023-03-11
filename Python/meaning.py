from PyDictionary import PyDictionary

# Call PyDictionary class
dc = PyDictionary()

# Get meaning of word "Code"
file=open("data.txt","r")
words=file.read()
splits=words.split()
for split in splits:
    mn = dc.meaning(split)
    if (mn==None):
        pass
    else:
        print(split+" = "+str(mn)+"\n")
