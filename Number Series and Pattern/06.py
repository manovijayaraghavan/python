# Question 6: Geometric Progression Printer
# Given first term a, ratio r, and number of terms n, print the geometric progression.

a, r, n = map(int, input().split())
series = []
term = a
for _ in range(n):
    series.append(term)
    term *= r
print(*series)
