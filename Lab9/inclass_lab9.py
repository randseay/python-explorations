"""
Author: Rand Seay
Objective:
"""

"""
dict1 = {'new1': 1111, 'new2': 2222}
print(dict1)
dict1['new3'] = 3333
print(dict1)
print(dict([('key1',1111),('key2',2222),('key3',3333),('key4',4444)]))
print({x: x**2 for x in (2,4,6)})
print(dict(type1=1111,type2=2222,type3=3333))
dict1['new4'] = 4444
print(dict1)
dict1['new3'] = 5555
print(dict1)
dict1[1] = 7777
print(dict1)
dict1['a'] = 7777
print(dict1)
del dict1['new3']
print(dict1)
print(dict1.keys())
print(dict1.values())
print('new2' in dict1)
print(dict1.items())

list = [1,2,3,4,5]
list.append(x)
list.insert(i, x)
print(list[-1])
insert(len(list), x) #append
list.remove(x)
list.pop(x)
"""

"""
Create file1 and file2
In which file you want to write a number?
Enter number
Write number into specified file
At the end close the file
Open both files again
Read all number from file and store into list
Sort the list

Write a program that takes a filename and
string from user and returns a number of times
the string is occur in the file(ignore
special characters and case(upper/lower case) of
the words)

Give options for the user till it press 'Y' and
stop asking once user presses 'N'

1. insert
2. remove
3. sort
4. print values
5. print keys
6. search whether key is exist or not
    Enter key
7. print all items from the list
"""

while True:
    whichFile = input("Would you like to write numbers to file1 or file2?\n> ")

    if whichFile == "file1":
        fileContents = open("file1.txt", "w")
        break
    elif whichFile == "file2":
        fileContents = open("file2.txt", "w")
        break
    else:
        print('\nThat is not a valid file, please enter either "file1" or "file2".\n')

count = 0
while True and count < 10:
    try:
        yourNumber = int(input("Please enter a number to add to the file.\n> "))

        fileContents.write(str(yourNumber) + "\n")
        count += 1
        if count >= 10:
            break
    except ValueError :
        print("\nThat is not a valid number, please try again.\n")
fileContents.close()

file1 = open("file1.txt")
file1Contents = []
for line in file1:
    file1Contents.append(int(line.strip()))

file2 = open("file2.txt")
file2Contents = []
for line in file2:
    file2Contents.append(int(line.strip()))

contentList = file1Contents + file2Contents
contentList.sort()
print("Here is the sorted list of the contents of both files.\n>", contentList)
