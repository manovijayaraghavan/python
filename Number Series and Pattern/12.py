# Question 2: Number Increasing Triangle
# Print a triangle where row i contains the number i repeated i times.

n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)
