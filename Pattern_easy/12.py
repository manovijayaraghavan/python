# Question: Write a Python program for Pattern easy problem 12.

n = int(input())
for i in range(1,n+1):
    if (i%2==0):
        print(-i,end=" ")
    else:
        print(i,end=" ")
    
