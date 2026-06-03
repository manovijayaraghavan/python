# Question 15: Replace Each Element by Product of Others
n=int(input())
a=list(map(int,input().split()))
r=[]
for i in range(n):
    p=1
    for j in range(n):
        if i!=j:p*=a[j]
    r.append(p)
print(*r)