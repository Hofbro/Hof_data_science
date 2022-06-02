"""Game guess a number"""

import numpy as np

number = np.random.randint(1, 101) # choosing a number

# attempt counter
count = 0

while True:
    count+=1
    predict_number = int(input('Guess a number from 1 to 100\n'))
    
    if predict_number > number:
        print("The number is less!")
        
    elif predict_number < number:
        print("The number is more!")
        
    else:
        print(f"You god damn right! The number is {number}. You made {count} attempts!")
        break #End game
    
    
    
    