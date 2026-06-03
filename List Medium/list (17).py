# Question 17: Minimum Difference Pair
n=int(input())
a=sorted(map(int,input().split()))
print(min(a[i]-a[i-1] for i in range(1,n)))