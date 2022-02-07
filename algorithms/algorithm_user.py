def run():
    print("Welcome to square root!")
    objective = int(input("Write a number: "))
    print("Choose your method:\n A. Approximation \n B. Binary Search \n E. Enumeration")
    command = input("Please, choose an option: ").lower()
    
    
    
    if command == 'a':
        epsilon = 0.01
        step = epsilon**2
        answer = 0.0
    
        while abs(answer**2 - objective) >= epsilon and answer <= objective:
	        answer += step

        if abs(answer**2 - objective) >= epsilon:
    	    print('No answer was found')
        else:
	        print(f'The square root of {objective} is {answer}')

    elif command == 'b':
        
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
    
    elif command == 'e':
        response = 0

        while response**2 < objective:
	        response += 1

        if response**2 == objective:
	        print(f'The square root of {objective} is {response}')
        else:
	        print(f'{objective} doesnt have a proper square root')

    else:
        print("Invalid command")
        
if __name__=="__main__":
    run()
