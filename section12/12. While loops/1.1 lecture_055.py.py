
### Tony Staunton
### Using while loops

current_number = 1
print(current_number)
while current_number <= 55:	
	current_number += 1
	if current_number % 5 == 0 and current_number < 55: print(current_number , ", " , (current_number + 1) , ",")
	elif current_number % 5 == 0 and current_number == 55: print(current_number)