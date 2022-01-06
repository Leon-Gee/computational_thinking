def factorial(number):
	"""Calculate the factor of a number
	param number int > 0
	returns n!
	"""
	if number == 1:
		return 1

	return number * factorial(number -1)


if __name__ == "__main__":
	number = int(input("Write a number: "))
	print(factorial(number = number))
