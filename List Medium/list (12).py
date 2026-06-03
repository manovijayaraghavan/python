# Question 12: Frequency Sort by First Appearance
n=int(input())
a=list(map(int,input().split()))
print(*sorted(a,key=lambda x:(-a.count(x),a.index(x))))