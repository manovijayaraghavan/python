# Question 8: Hollow Square Pattern
# Print a hollow square of size n using stars.

n = int(input())
for i in range(n):
    row = []
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            row.append("*")
        else:
            row.append(" ")
    print("".join(row))
