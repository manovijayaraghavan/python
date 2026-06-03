# Question: Write a Python program for Loop Easy problem 14.

n,d = map(int,input().split())
freq = 0
temp = n
while(temp>0):
    a = temp%10
    if (a==d):
        freq += 1
    temp//=10
print(freq)
    
    
