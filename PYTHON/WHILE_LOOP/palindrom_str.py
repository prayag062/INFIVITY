word="racecdr"
i=0
j=len(word)-1

while i<j:
    if(word[i]==word[j]):
        i+=1
        j-=1
        print("It is a palindrom")
        
    else:
        i+=1
        j-=1
        print("It is not a palindrom")
        