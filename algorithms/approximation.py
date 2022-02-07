objective = int(input('write a number: '))

epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
	answer += step

if abs(answer**2 - objective) >= epsilon:
	print('No answer was found')
else:
	print(f'The square root of {objective} is {answer}')
