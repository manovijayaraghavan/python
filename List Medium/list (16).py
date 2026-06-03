# Question 16: Check List Mountain Shape
n=int(input())
a=list(map(int,input().split()))
i=0
while i+1<n and a[i]<a[i+1]: i+=1
if i==0 or i==n-1: print("NO")
else:
    while i+1<n and a[i]>a[i+1]: i+=1
    print("YES" if i==n-1 else "NO")