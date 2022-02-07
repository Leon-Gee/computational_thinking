objective = int(input('write a number: ' ))

epsilon= 0.01
low = 0.0
high = max(1.0, objective)
answer = (high + low) / 2

while abs(answer**2 - objective) >= epsilon:
	if answer**2 < objective:
		low = answer
	else:
		high = answer

	answer = (high + low) / 2

print(f'square root of {objective} is {answer}')
