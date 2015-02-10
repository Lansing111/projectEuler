num1 = 1
num2 = 1
addition = 0
sum = 0
while num2 < 4000000:
    addition = num1 + num2 
    num1 = num2
    num2 = addition
    if num2 % 2 == 0:
       sum = sum + num2 
print (sum)
