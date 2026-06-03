# Question 2: Rotate List by K Positions
n=int(input())
a=list(map(int,input().split()))
k=int(input())%n
print(*(a[-k:]+a[:-k]))