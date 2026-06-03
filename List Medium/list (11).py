# Question 11: Merge Two Sorted Lists
n=int(input()); a=list(map(int,input().split()))
m=int(input()); b=list(map(int,input().split()))
i=j=0; r=[]
while i<n and j<m:
    if a[i]<=b[j]: r.append(a[i]); i+=1
    else: r.append(b[j]); j+=1
print(*(r+a[i:]+b[j:]))