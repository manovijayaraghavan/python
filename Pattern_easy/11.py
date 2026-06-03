# Question: Write a Python program for Pattern easy problem 11.

a,r,n = map(int,input().split())
c = a
for i in range(n):
    print(c,end=" ")
    c*=r
    
