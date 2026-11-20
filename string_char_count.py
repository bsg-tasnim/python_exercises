#Create a function that takes a string and returns a count of 
# how many times each character appears. 
# Ignore spaces and make it case-insensitive.
text = "Python Programming"
text=text.lower().replace(" ","")

result={}
for i in text:
    if i in result:
        result[i]+=1

    else:
        result[i]=1

print(result)
