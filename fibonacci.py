##########################################################################################################################################################################################################
####### source file name: fibonacci.py
####### objective: to find the Fibonacci numbers
####### created date: 25-august-2024
####### last modified date: 25-august-2024
####### repo: https://github.com/franciscl123/pythonportfolio
##########################################################################################################################################################################################################
def fibonacci(number):
	if (number == 1 or  number == 2):
		return number
	else:
		return fibonacci(number - 1) + fibonacci(number - 2)

nums = range(1,100,1)
for x in nums:
	print(str(fibonacci(x)))

