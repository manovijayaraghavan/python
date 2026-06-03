# Question 7: Floyd Number Triangle
# Print Floyd triangle with n rows using increasing numbers starting from 1.

n = int(input())
num = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(str(num))
        num += 1
    print(" ".join(row))
