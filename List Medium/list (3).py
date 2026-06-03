# Question 3: Leaders in a List
n=int(input())
a=list(map(int,input().split()))
m=a[-1]
r=[m]
for i in a[-2::-1]:
    if i>m:
        r.append(i)
        m=i
print(*r[::-1])