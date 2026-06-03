# Question 10: Positive and Negative Count
# Count positive and negative numbers.

n=int(input())
a=list(map(int,input().split()))

pos=0
neg=0

for i in a:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1

print(pos,neg)