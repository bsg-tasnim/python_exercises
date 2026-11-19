#Given a list of strings, use a single list comprehension to extract strings 
# that meet two criteria: they must be longer than 5 characters AND 
# they must start with a vowel (a, e, i, o, u).

x=["apple", "education", "ice", "ocean", "python", "umbrella"]

y=[]

for i in x:
    if len(i)>5 and i[0].lower() in "aeiou":
        y.append(i)

print(y)