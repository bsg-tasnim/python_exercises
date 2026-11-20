#Write a function that removes duplicate elements from a list but maintain the list order. 
# You cannot use set() because sets do not maintain the original order of elements.

list=[1, 2, 2, 3, 1, 4, 2]

new=[]
for i in list:
    if i not in new:
        new.append(i)
print(new)