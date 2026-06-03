# Question 15: Wind Chill Factor
t=int(input());v=int(input())
w=35.74+0.6215*t+(0.4275*t-35.75)*(v**0.16)
print("%.2f"%w)
