user = input ("enter the string")
charactercount = 0
wordcount = 1
for i in user:
    charactercount = charactercount +1
    if (i == " "):
        wordcount = wordcount +1

print (wordcount)
print (charactercount)

