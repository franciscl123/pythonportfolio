##########################################################################################################################################################################################################
####### source file name: smallestmultiple.py
####### objective: 
####### created date: 17-Sep-2024
####### last modified date: 17-Sep-2024
####### repo: https://github.com/franciscl123/pythonportfolio
####### reference: https://projecteuler.net/problem=5
##########################################################################################################################################################################################################
import time
def ismultiple(number):
	for j in range(1,20):
		if (number % j != 0):
			return False
	return True


x = 10000000000
min = x
for j in range(x,1,-1):
	if ismultiple(j):
		print(str(j))
#		time.sleep(1)
#		if j < min:
#			min = j
#print(str(min))
