# Question 6: Longest Increasing Continuous Segment
n=int(input())
a=list(map(int,input().split()))
ans=cur=1
for i in range(1,n):
    cur=cur+1 if a[i]>a[i-1] else 1
    ans=max(ans,cur)
print(ans)