# Question 1: Shopping Bill Total
# Find total price of all items stored in a list.

n=int(input())
prices=list(map(int,input().split()))
print(sum(prices))