# Question: Write a Python program for Operators problem 2.

price_1=float(input())
price_2=float(input())
discount=int(input())
total_amount=price_1+price_2
discounted_price=total_amount-(total_amount*(discount/100))
amount_saved=total_amount-discounted_price
print("%.2f"%total_amount)
print("%.2f"%discounted_price)
print("%.2f"%amount_saved)
