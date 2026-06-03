# Question: Write a Python program for Loop Easy problem 7.

n = int(input())
temp = n
total = 0
while (temp>0):
    dig = temp%10
    fact = 1
    temp//=10
    for i in range(1,dig+1):
        fact*=i
    total+=fact
if (n==total):
    print("Yes")
else:
    print("No")
    
