# Question 3: Count Even Numbers
# Count how many numbers in the list are even.

n=int(input())
a=list(map(int,input().split()))
count=0
for i in a:
    if i%2==0:
        count+=1
print(count)