word=input("enter a word")
character=input("enter a character from the word")
count=0
i=0
while i<len(word):
    if word[i]==character:
        count=count+1
    i=i+1
print(count)        
        
    

