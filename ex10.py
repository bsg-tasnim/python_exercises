#Write a program that takes two separate dictionaries and merges them into one single dictionary.

dict1= {
    "name": "Jarifa",
    "age": 23
}

dict2={
    "city": "Dhaka"
}

dict3= dict1 | dict2

print(dict3)