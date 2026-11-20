#Create a new list from two given lists such that the new list contains odd numbers from the first list 
# and even numbers from the second list.

l1=[10,12,15,17,20]
l2=[3,5,6,8,9]

l3=[]
for i in l1:
    if i%2!=0:
        l3.append(i)

for j in l2:
    if j%2==0:
        l3.append(j)

print(l3)
