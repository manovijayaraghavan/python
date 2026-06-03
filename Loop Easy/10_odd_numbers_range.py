# Question 10: Print Odd Numbers in a Range

a, b = map(int, input().split())
start = a if a % 2 == 1 else a + 1
print(*range(start, b + 1, 2))
