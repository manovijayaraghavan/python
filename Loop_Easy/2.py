# Question: Write a Python program for Loop Easy problem 2.

import math
n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
print(math.factorial(n))
