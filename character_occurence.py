word=input("Enter a word=")
for i in range(len(word)):
    char=word[i]
    count=0
    for j in range(len(word)):
        if word[j]==char:
            count+=1
    print("Character",char,"appears",count,"times.")