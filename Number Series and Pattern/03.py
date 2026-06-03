# Question 3: Print Odd Numbers in Reverse
# Write a program to print all odd numbers from n down to 1.

n = int(input())
start = n if n % 2 == 1 else n - 1
print(*range(start, 0, -2))
