"""Game "Guess number"
computer is able to guess the number by itself"""

import numpy as np

def guess_number(number) -> int:
    """Computer guesses the number

    Args:
        number (int): Random number from 1 to 100

    Returns:
        int: Number of attempts
    """

    predict_number = 50 # First prediction
    lower_limit = 1
    upper_limit = 101
    count = 0 # Number of attempts

    while True:
        count+=1 
        
        if predict_number > number:
            upper_limit = upper_limit -(upper_limit-lower_limit)//2 # Reducing the upper range limit
            predict_number = (upper_limit+lower_limit)//2
            
        elif predict_number < number:
            lower_limit = lower_limit + (upper_limit-lower_limit)//2 # Reducing the lower range limit
            predict_number = (upper_limit+lower_limit)//2

        else:
            break #End game
        
    return count

def score_game(guess_number) -> int:
    """Average attempts meter

    Args:
        guess_number (func): Guessing function

    Returns:
        int: Average attempts
    """
    count_ls = []
    np.random.seed(1)    # fixing seed for reproducibility
    random_array = np.random.randint(1,101, size=(1000))   # Setting array of numbers and number of repeats
    
    for number in random_array:
        count_ls.append(guess_number(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorithm average correct guessing is: {score} attempts')
    return score

if __name__ == '__main__':
    #  RUN
    score_game(guess_number)