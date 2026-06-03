# Question: Write a Python program for Loop Easy problem 12.

n = int(input())
temp = n
total = 0

while(temp>0):
    dig = temp%10
    fact = 1
    for i in range(1,dig+1):
        fact*=i
    total+=fact
    temp//=10
if (total==n):
    print("yes")
else:
    print("No")
