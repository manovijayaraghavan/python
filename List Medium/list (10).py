# Question 10: Maximum Difference with Larger Element After Smaller
n=int(input())
a=list(map(int,input().split()))
mn=a[0]; ans=0
for i in a:
    ans=max(ans,i-mn)
    mn=min(mn,i)
print(ans)