import math
from primeChecker import findAllPrimes, findAllComposites, findLargestPrimeNumber, findPrimeFactors

def smallestMultiple(n):
	'''Determine the smallest positive number divisible by all integer factors from 1 to n inclusive.'''
	myFactors = []
	myPrimeFactors = findAllPrimes(n)
	myCompositeFactors = findAllComposites(n)
	myFactors = myPrimeFactors

	# Checks to see if the product of all factors are divisible by the composites
	for composite in myCompositeFactors:
		myMultiple = multiplyAll(myFactors)
		primesOfComposite = findPrimeFactors(composite)
		if myMultiple % composite != 0:
			myFactors += primesOfComposite

	return multiplyAll(myFactors)

def multiplyAll(myList):
	'''Multiplies all the numbers in list myList.'''
	product = 1
	for item in myList:
		product *= item
	return product

# Driver
myInput = input('Insert integer of interest...')
a = smallestMultiple(myInput)
print("Here's the multiple...")
print(a)
