import numpy as np

number = np.random.randint(1, 101) # choosing a number

# attempt counter
count = 0
predict_number = 50

while True:
    count+=1 
    
    if predict_number > number:
        predict_number = np.random.randint(51,101)
        
    elif predict_number < number:
        predict_number = np.random.randint(1,50)
        
    else:
        print(f"You god damn right! The number is {number}. You made {count} attempts!")
        break #End game