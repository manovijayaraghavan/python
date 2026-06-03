# Question 9: Split List Around Pivot
n=int(input())
a=list(map(int,input().split()))
p=int(input())
print(*([i for i in a if i<p]+[i for i in a if i==p]+[i for i in a if i>p]))