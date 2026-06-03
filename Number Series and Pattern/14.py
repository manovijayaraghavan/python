# Question 4: Left-Aligned Alphabet Triangle
# Print a triangle of alphabets starting from A in every row.

n = int(input())
for i in range(1, n + 1):
    print("".join(chr(ord('A') + j) for j in range(i)))
