#Write a function that determines if two strings are anagrams
#(contain the exact same characters in a different order).

word1 = "listen"
word2 = "silent"

sorted1= "".join(sorted(word1))
sorted2= "".join(sorted(word2))

if sorted1==sorted2:
    print("Anagram")

else:
    print("Not Anagram")