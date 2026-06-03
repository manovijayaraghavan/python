# Question 7: Remove Duplicates
# Print unique elements in their first appearing order.

n=int(input())
a=list(map(int,input().split()))

res=[]
for i in a:
    if i not in res:
        res.append(i)

print(*res)