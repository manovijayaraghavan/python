# Question 3: Inverted Star Triangle
# Print an inverted triangle of stars with n rows.

n = int(input())
for i in range(n, 0, -1):
    print("*" * i)
