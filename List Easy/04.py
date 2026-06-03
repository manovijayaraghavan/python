# Question 4: Reverse the List
# Print list elements in reverse order.

n=int(input())
a=list(map(int,input().split()))
print(*a[::-1])