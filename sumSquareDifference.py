def sumSquareDifference(n):
	'''Returns the difference between the sum of squares of all natural numbers less than
	or equal to n and the square of the sum of all natural numbers less than or equal to n.'''
	list_of_naturals = []
	square_of_naturals = []

	for i in range(1,n+1):
		list_of_naturals.append(i)
		square_of_naturals.append(i**2)

	square_of_sum = (sum(list_of_naturals))**2
	difference = square_of_sum - sum(square_of_naturals)
	return difference

# Driver
my_input = input('Input a natural number...')
print(sumSquareDifference(my_input))