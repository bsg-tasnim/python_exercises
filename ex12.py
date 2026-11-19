#Write a function that merges two dictionaries. 
# If a key exists in both dictionaries, sum their values. 
# If a key exists in only one, include it as is.

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

dict_new=dict_a.copy()

for key in dict_b:
    if key in dict_new:
        dict_new[key]+=dict_b[key]

    else:
        dict_new[key]=dict_b[key]

print(dict_new)

