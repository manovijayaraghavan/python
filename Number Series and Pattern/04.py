# Question 4: Multiplication Table Series
# Write a program to print the first 10 multiples of a given number x.

x = int(input())
print(*[x * i for i in range(1, 11)])
