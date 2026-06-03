# Question 13: Remove Elements Present in Second List
n=int(input()); a=list(map(int,input().split()))
m=int(input()); b=set(map(int,input().split()))
r=[i for i in a if i not in b]
print(*r if r else ["EMPTY"])