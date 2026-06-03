# Question 6: Inverted Centered Pyramid
# Print an inverted centered pyramid of stars.

n = int(input())
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
