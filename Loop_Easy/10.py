# Question: Write a Python program for Loop Easy problem 10.

I,R = map(int,input().split())
prime = 0
for i in range(I,R+1):
    if (i>1):
        p = True
        for j in range(2,i):
            if (i%j==0):
                p = False
                break
        if (p):
            prime+=1
print(prime)
    
