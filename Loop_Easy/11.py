# Question: Write a Python program for Loop Easy problem 11.

I,r = map(int,input().split())
count = 0

for i in range(I,r+1):
    if (i>1):
        a = 0
        for j in range(1,i):
            if (i%j==0):
                a+=j
        if (a==i):
           count+=1
print(count)
          
        
    
