# Question 4: Find Missing Number from 1 to N
n=int(input())
a=list(map(int,input().split()))
print(n*(n+1)//2-sum(a))