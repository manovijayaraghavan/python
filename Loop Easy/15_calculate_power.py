# Question 15: Calculate Power

base, exponent = map(int, input().split())
result = 1
for _ in range(exponent):
    result *= base
print(result)
