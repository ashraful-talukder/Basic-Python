list1=[12,12.5,"This is a string"]

print(list1)

#Inserting elements

list1.append(50)

list1.insert(2,"Ashraful")
print(list1)

#Updating list

list1[1]=20
print(list1)

#deleting list elements

list1.pop()
print(list1)

del list1[2]

#check length

print(len(list1))

for i in range(0,len(list1)):
    print(list1[i])

for j in list1:
    print(j)