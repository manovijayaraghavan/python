# Question: Write a Python program for Operators problem 9.

p=int(input())
r=int(input())
n=int(input())
si=(p*n*r)/100
amount=p+si
dis=si*0.02
final_amount=amount-dis
print("%.2f"%si)
print("%.2f"%amount)
print("%.2f"%dis)
print("%.2f"%final_amount)
