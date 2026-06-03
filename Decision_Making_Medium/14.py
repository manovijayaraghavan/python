# Question: Write a Python program for Decision making problem 14.

ch = input()
if ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
    print("Alphabet")
elif (ch >= '0' and ch <= '9'):
    print("Number")
else:
    print("Special Character")


