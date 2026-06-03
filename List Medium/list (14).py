# Question 14: Find Subarray with Given Sum
n=int(input())
a=list(map(int,input().split()))
t=int(input())
s=l=0
for r in range(n):
    s+=a[r]
    while s>t:
        s-=a[l]; l+=1
    if s==t:
        print(l+1,r+1)
        break
else:
    print(-1)