# Question 7: Squares Series
# Write a program to print the first n square numbers.

n = int(input())
print(*[i * i for i in range(1, n + 1)])
