#key -value pairs

dict1={}

#Adding elements to the dictionary

dict1['apple']="Apple is a fruit"
dict1['orange']="Orange is a color"
dict1['daffodil']="Daffodil is the name of an university"
dict1['python']="Python is a programming language"

print(dict1)

print(dict1['apple'])

print(dict1.get("apple"))

print(dict1.get("hello"))

print(dict1.get("apple","key doesn't exist"))

print(dict1.get("hello","key doesn't exist"))

#deleting from dictionary

del dict1['apple']

len(dict1)

listOfKeys = list(dict1.keys())

listOfValues = list(dict1.values())

for key in dict1.keys():
    print(dict1[key])


for value in dict1.values():
    print(value)