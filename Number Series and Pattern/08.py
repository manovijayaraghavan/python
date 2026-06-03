# Question 8: Alternating Sign Series
# Print the first n terms of the series: 1, -2, 3, -4, 5, -6...

n = int(input())
series = [i if i % 2 == 1 else -i for i in range(1, n + 1)]
print(*series)
