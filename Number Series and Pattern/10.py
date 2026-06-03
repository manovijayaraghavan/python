# Question 10: Prime Number Series
# Write a program to print the first n prime numbers using nested loops.

n = int(input())
primes = []
num = 2
while len(primes) < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1
print(*primes)
