# Question: Write a Python program for Loop Easy problem 9.

n = int(input())
low = 0
norm = 0
high = 0
for i in range(n):
    j = int(input())
    if (j<100):
        low+=1
    elif (j>=100 and j<=300):
        norm+=1
    else:
        high+=1
print(low)
print(norm)
print(high)
    
