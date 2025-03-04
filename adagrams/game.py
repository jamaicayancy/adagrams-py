import random

LETTER_POOL = {

    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}      



score_chart = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

# Wave 1

def draw_letters():
    new_list =[]

    while len(new_list) <10:
        letter  = (random.choices(list(LETTER_POOL.keys()), weights = list(LETTER_POOL.values()), k=1))[0]
        if new_list.count(letter) < LETTER_POOL[letter]:       
            new_list.append(letter)
        
    return(new_list)

# Wave 2

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    if len(word) > len(letter_bank_copy):
        return False
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False

    return True

# Wave 3

def score_word(word):

    score = 0
    if 7 <= len(word) <= 10:
        score += 8
    for letter in word.upper():
        if letter.isalpha():
            score += score_chart.get(letter)
    return score

# Wave 4

def get_highest_word_score(word_list):

    top_score = 0
    winner_list = []


    for i in range(len(word_list)):
        word = word_list[i]
        score = score_word(word_list[i]) 
        if score_word(word) > top_score:
            top_score = score 
    
    for i in range(len(word_list)):
        if score_word(word_list[i]) == top_score:
            winner_list.append(word_list[i])
    
    if len(winner_list) == 1:
        winner = (winner_list[0])
    
    if len(winner_list) > 1:
        winner1 = max(winner_list, key=len)
        winner2 = min(winner_list, key=len)
        if len(winner1) == 10:
            winner = winner1
        else:
            winner = winner2
    
    winner_score = score_word(winner)

    return(winner, winner_score)

