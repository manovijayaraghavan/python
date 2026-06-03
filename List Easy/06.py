# Question 6: Sum of Odd Numbers
# Find the sum of only odd numbers in the list.

n=int(input())
a=list(map(int,input().split()))

s=0
for i in a:
    if i%2!=0:
        s+=i
print(s)