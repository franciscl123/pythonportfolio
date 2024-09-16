##########################################################################################################################################################################################################
####### source file name: palindromeproduct.py
####### objective: 
####### created date: 16-Sep-2024
####### last modified date: 16-Sep-2024
####### repo: https://github.com/franciscl123/pythonportfolio
####### reference: https://projecteuler.net/problem=4
##########################################################################################################################################################################################################
def ispalindrome(number):
	if str(number)==reversestring(str(number)):
		return True
	else:
		return False

def reversestring(mystring):
	return mystring[::-1]

x = 999
y = 999
max = 0
found = False
for j in range(x,100,-1):
	for k in range(y,100,-1):
		if ispalindrome(j * k):
			if (j * k > max):
				max = j * k

print(str(max))
