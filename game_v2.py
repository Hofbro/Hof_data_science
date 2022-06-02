"""Game guess a number
done by comp
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Random number prediction

    Args:
        number (int, optional): Predicted number. Defaults to 1.

    Returns:
        int: Attempts
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)   # predicted number
        if number == predict_number:
            break # exit if prediction is right
    return(count)


def score_game(random_predict) -> int:
    """Average attempts meeter

    Args:
        randome_predict (_type_): prediction function

    Returns:
        int: average attempts
    """
    count_ls = []
    np.random.seed(1)    # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000))   # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorithm average mean win predictions to: {score} attempts')
    return score

if __name__ == '__main__':
    #  RUN
    score_game(random_predict)
    
    
    