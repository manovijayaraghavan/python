# Question 20: K Most Frequent Elements
n=int(input())
a=list(map(int,input().split()))
k=int(input())
u=list(set(a))
u.sort(key=lambda x:(-a.count(x),x))
print(*u[:k])