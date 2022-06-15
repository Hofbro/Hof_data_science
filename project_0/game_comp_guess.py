import numpy as np
def guess_number(number):

n = 101
predict_number = n//2
count = 0
low_limit = 1
high_limit = n

while True:
    count+=1 
    
    if predict_number > number:
        high_limit -= (high_limit-low_limit)//2
        predict_number = (high_limit+low_limit)//2
        
    elif predict_number < number:
        low_limit += (high_limit-low_limit)//2
        predict_number = (high_limit+low_limit)//2

    else:
        break #End game
    
    return count

def score_game(random_predict) -> int:
    """Average attempts meeter

    Args:
        random_predict (_type_): prediction function

    Returns:
        int: average attempts
    """
    count_ls = []
    np.random.seed(1)    # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000))   # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorithm average win predictions is: {score} attempts')
    return score

if __name__ == '__main__':
    #  RUN
    score_game(random_predict)