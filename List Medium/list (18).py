# Question 18: Rearrange Alternating Positive and Negative
n=int(input())
a=list(map(int,input().split()))
p=[i for i in a if i>0]; neg=[i for i in a if i<0]
r=[]
while p and neg:
    r.append(p.pop(0)); r.append(neg.pop(0))
print(*(r+p+neg))