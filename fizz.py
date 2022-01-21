def response( input ) :
	# Enter your code here
	response = []
	for i in range(1, input + 1):
		if (i % 3 == 0) and (i % 5 == 0):
			response.append('FizzBuzz')
		elif i % 3 == 0:
			response.append('Fizz')
		elif i % 5 == 0:
			response.append('Buzz')
		else:
			response.append(i)
	return response