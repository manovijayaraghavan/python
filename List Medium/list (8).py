# Question 8: Second Largest Distinct Element
n=int(input())
a=sorted(set(map(int,input().split())),reverse=True)
print(a[1] if len(a)>1 else -1)