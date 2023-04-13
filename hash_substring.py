import sys

print("Enter 'I' to input from keyboard, or 'F' to input from file")
choice = input().strip()

input1 = ""
input2 = ""
if choice == "I":
    print("Enter pattern:")
    input1 = input().strip()

    print("Enter text:")
    input2 = input().strip()

elif choice == "F":
    print("Enter file name: ")
    try:
        fileName = input().strip()
        with open(fileName, 'r') as f:
            input1 = f.readline().strip()
            input2 = f.readline().strip()
            print("Firstline is : " + input1)
            print("Secondline is : " + input2)
    except:
        print("error")
        sys.exit(0)
else:
    print("wrong input")

len1 = len(input1)
len2 = len(input2)

i = 0
x = len1
y = 0
str = input2
while i < len2:
    try:
        str2 = str[y:x]
        x += 1
        y += 1
        if str2 == input1:
            print(i, end=" ")
        i += 1
    except:
        break