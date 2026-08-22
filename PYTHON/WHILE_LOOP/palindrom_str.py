word=input("Enter any letter or sentence: ")
l=0
r=len(word)-1
is_Palindrome = True

while l<r:

    if word[l] != word[r]:
        is_Palindrome=False
    l+=1
    r-=1


print(f" Palindrome string: {is_Palindrome}")

