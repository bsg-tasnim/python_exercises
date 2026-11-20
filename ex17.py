#Merge two dictionaries. 
# If they share a key, the new dictionary should store a list containing values from both dictionaries 
# instead of overwriting the first one.

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d3=d1.copy()
for key in d2:
    if key in d3:
        d3[key]=[d3[key], d2[key]]
    else:
        d3[key]=d2[key]

print(d3)