# Question 8: Second Largest Number
# Find second largest unique value.

n=int(input())
a=list(map(int,input().split()))

a=list(set(a))
a.sort()

if len(a)<2:
    print("NO SECOND LARGEST")
else:
    print(a[-2])