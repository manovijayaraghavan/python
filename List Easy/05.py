# Question 5: Search an Element
# Check whether target value exists in the list.

n=int(input())
a=list(map(int,input().split()))
target=int(input())

if target in a:
    print("FOUND")
else:
    print("NOT FOUND")