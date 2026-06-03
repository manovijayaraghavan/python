# Question: Write a Python program for Loop Easy problem 15.

n = int(input())
valid = 0
invalid = 0
total = 0
for i in range(n):
    i=int(input())
    if (i>0 and i%100==0):
        valid+=1
        total+=i
    else:
        invalid+=1


print(valid)
print(invalid)
print(total)

