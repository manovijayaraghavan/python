# Question: Write a Python program for Loop Easy problem 8.

n,k = map(int,input().split())
total = 0
expect = 0

for i in range(n):
    a = int(input())
    total+=a
    if (a>k):
        expect+=1
    
        
print(total)
print(expect)
