# Question: Write a Python program for Loop Easy problem 16.


s, inc, t = map(int, input().split())

total = 0
days = 0
daily_save = s


while total < t:
    total += daily_save
    days += 1
    daily_save += inc


print("Days Required:", days)
