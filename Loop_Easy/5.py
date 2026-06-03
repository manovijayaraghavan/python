# Question: Write a Python program for Loop Easy problem 5.

n = int(input())
a = n
rev = 0
while(a>0):
    dig = a%10
    rev = rev*10+dig
    a//=10
print(rev)
if (n == rev):
    print("yes")
else:
    print("No")

