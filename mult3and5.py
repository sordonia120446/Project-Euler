def special_sum(n):
	'''Takes in a number n.  Returns the sum of all multiples of 3 and 5 in [1,n]'''
	return sum(n)

def multiple_of_three(n):
	'''Returns a list of all multiples of 3 from [1,n].'''
	myMultiples = []
	for number in range(1,n):
		if number % 3 == 0 or number % 5 == 0:
			myMultiples.append(number)
	return sum(myMultiples)

# Driver
print('Takes in a number n.  Returns the sum of all multiples of 3 and 5 in [1,n]')
n = input('What number you want to check?')
print(multiple_of_three(n))