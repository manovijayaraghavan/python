# Question: Write a Python program for Loop Easy problem 1.

n,k = map(int,input().split())
vio = 0
high = 0
for i in range(n):
    a = int(input())
    if (a>k):
        vio += 1
    if (a>high):
        high = a
        
        
        
print("Violations:",vio)
print("Highest Transaction:",high)
    
