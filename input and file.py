inp=input("Enter a number:")
number1=int(inp)

number2=int(input("Enter another number:"))

print(number1+number2)

#File I/O

#Writing to file

inp= input("Enter some text:")

with open("textFile.txt","w") as f:
    f.write(inp)


with open("textFile.txt","a") as f:
    f.write(inp)

with open("textFile.txt","r") as f:
    print(f.read())
