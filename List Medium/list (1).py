# Question 1: Compress Consecutive Duplicates
n=int(input())
a=list(map(int,input().split()))
r=[a[0]]
for i in a[1:]:
    if i!=r[-1]:
        r.append(i)
print(*r)