##########################################################################################################################################################################################################
####### source file name: evenfibonacci.py
####### objective: to find the Fibonacci numbers which are even
####### created date: 25-august-2024
####### last modified date: 25-august-2024
####### repo: https://github.com/franciscl123/pythonportfolio
####### reference: https://projecteuler.net/problem=2
##########################################################################################################################################################################################################
def fibonacci(number):
	if (number == 1 or  number == 2):
		return number
	else:
		return fibonacci(number - 1) + fibonacci(number - 2)

def iseven(number):
	return(not number%2)
nums = range(1,100,1)
for x in nums:
        fib = fibonacci(x)
	if iseven(fib):
		print(str(fib))

