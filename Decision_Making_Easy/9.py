# Question: Write a Python program for Decision making problem 9.

B=int(input())
if(B>=0 and B<=10):
    print("Critical")
elif(B>=11 and B<=30):
    print("Low Battery")
else:
    print("Battery OK")
