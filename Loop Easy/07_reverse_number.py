# Question 7: Reverse a Number

n = int(input())
rev = 0
if n == 0:
    print(0)
else:
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print(rev)
