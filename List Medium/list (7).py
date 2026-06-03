# Question 7: Move All Zeros to End
n=int(input())
a=list(map(int,input().split()))
b=[i for i in a if i!=0]
print(*(b+[0]*(n-len(b))))