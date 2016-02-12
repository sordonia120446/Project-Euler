import math

def primeChecker(n):
	'''Checks to see if input n is a prime number.  Returns True if it is.'''
	try:
		n = int(n)
	except TypeError:
		print('Please input an integer!')
	if n <= 1:
		return False
	elif n == 2 or n == 3:
		return True
	elif (n % 2 ==  0) or (n % 3 == 0):
		return False
	elif n >= 5:
		cntr = 5
		limit = math.sqrt(n)
		while cntr < limit:
			if (n % cntr == 0) or (n % (cntr + 2) == 0):
				return False
			cntr += 6
		
	return True

def findAllPrimes(n):
	'''Returns all positive prime factors less than input integer n.'''
	myPrimes = []
	cntr = 2
	while cntr <= n:
		if primeChecker(cntr):
			myPrimes.append(cntr)
		cntr += 1
	return myPrimes

def findPrimeFactors(n):
	myPrimes = []
	cntr = 2
	while cntr <= n:
		if primeChecker(cntr) and (n % cntr == 0):
			myPrimes.append(cntr)
		cntr += 1
	return myPrimes

def findAllComposites(n):
	'''Returns all positive composite factors less than integer n.'''
	myPrimeFactors = findAllPrimes(n)
	myComposites = []
	cntr = 2
	while cntr <= n:

		# Loop through all prime factors
		index = 0
		while index < len(myPrimeFactors):
			factor = myPrimeFactors[index]
			if (isFactor(cntr,factor)) and (cntr > factor):
				myComposites.append(cntr)
				break
			index += 1
		cntr += 1
	return myComposites

def findLargestPrimeNumber(n):
	'''Find the largest prime number factor of input n'''
	if primeChecker(n):
		return n
	else:
		cntr = 2
		while cntr < math.sqrt(n):
			if isFactor(n,cntr):
				n /= cntr
				return findLargestPrimeNumber(n)
			else:
				cntr += 1

def isFactor(n,factor):
	if n % factor == 0:
		return True
	else:
		return False

# Driver
# a = input('Input an integer to find its greatest prime factor..')
# a = findLargestPrimeNumber(a)
# print(a)
# print(primeChecker(a))