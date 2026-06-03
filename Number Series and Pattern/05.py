# Question 5: Arithmetic Progression Printer
# Given first term a, common difference d, and number of terms n, print the arithmetic progression.

a, d, n = map(int, input().split())
series = [a + i * d for i in range(n)]
print(*series)
