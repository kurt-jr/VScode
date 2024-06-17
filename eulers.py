#Euler's 1
x = 0;
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        x += i;
print(x)

#Euler's 2
sum = 0     # Variable to hold sum
num1 = 0;   # First number
num2 = 1;   # Second number
 
# While the second number is less than 4000000
while num2 < 4000000:
    #incrementing numbers
    temp = num1
    num1 = num2
    num2 = num1 + temp
 
 
    # If the number is even, add to sum
    if(num1%2 == 0):
        sum += num1
 
# Print
print('The sum is: ' + str(sum))