# Question 5: Centered Star Pyramid
# Print a pyramid with n rows. Each row has leading spaces and odd number of stars.

n = int(input())
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
