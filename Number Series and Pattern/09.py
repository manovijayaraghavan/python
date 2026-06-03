# Question 9: Fibonacci Series Printer
# Write a program to print the first n Fibonacci numbers starting from 0 and 1.

n = int(input())
fib = []
a, b = 0, 1
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print(*fib)
