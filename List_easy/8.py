# Question: Write a Python program for List easy problem 8.

n = int(input())
a = list(map(int,input().split()))
pos = 0
neg = 0
for i in a:
    if (i>0):
        pos+=1
    elif (i<0):
        neg+=1
        
print(pos,neg)
        
