# Question 10: Hollow Diamond Pattern
# Print a hollow diamond pattern of height 2*n-1 using stars on the border only.

n = int(input())

# Upper half including middle
for i in range(1, n + 1):
    spaces = " " * (n - i)
    if i == 1:
        print(spaces + "*")
    else:
        inner = " " * (2 * i - 3)
        print(spaces + "*" + inner + "*")

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    if i == 1:
        print(spaces + "*")
    else:
        inner = " " * (2 * i - 3)
        print(spaces + "*" + inner + "*")
