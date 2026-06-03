# Question 9: List Rotation by One
# Move the last element to first position.

n=int(input())
a=list(map(int,input().split()))

a=[a[-1]]+a[:-1]
print(*a)