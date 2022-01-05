objective = int(input("Write a number: "))
response = 0

while response**2 < objective:
	response += 1

if response**2 == objective:
	print(f'The square root of {objective} is {response}')
else:
	print(f'{objective} doesnt have a proper square root')

