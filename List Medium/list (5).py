# Question 5: Count Pairs with Given Sum
n=int(input())
a=list(map(int,input().split()))
target=int(input())
d={}
c=0
for i in a:
    c+=d.get(target-i,0)
    d[i]=d.get(i,0)+1
print(c)