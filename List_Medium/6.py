# Question: Write a Python program for List Medium problem 6.

n = int(input())
arr = list(map(int,input().split()))
n_sum = 0
e_sum = 0
for i in range(1,n+1):
    n_sum += i
for j in arr:
    e_sum += j

r = n_sum - e_sum
print(r)
