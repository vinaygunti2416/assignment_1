# Write a Python program to get the Fibonacci series between 0 to 50


n=50
num1 = 0
num2 = 1
next_number = 0

while next_number <= n:
	print(next_number, end=" \t")
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()


