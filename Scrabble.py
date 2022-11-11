from random import choice
from string import ascii_uppercase

#task 1
def calculate_score(word):
    if not word:
        return 0
    points_For_Letter = {
        1: "EAIONRTLSU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ" 
    }
    
    result = 0
    for letter in word:
        for x in points_For_Letter:
            if points_For_Letter[x].__contains__(letter):
                result += int(x) 
    
    return result

def build_rack_from_alphabet():
    tiles = []
    for i in range(7):
        letter = choice(ascii_uppercase)
        tiles.append(build_tile(letter))
    return tiles
     
def build_tile(letter):
    if not letter:
        return None
    else:
        return { 
        'letter': letter,
        "points": calculate_score(letter)  
        }

def build_tile_set(amount, letter):
    if not amount or not letter:
        return None
    else:
        tile_set = []
        for i in range(amount):
            tile_set.append(build_tile(letter))
        return tile_set

def build_bag(distribution):
    bag = []
    for item in distribution: 
        amount = list(item.keys())[0] 
        letters = item[amount]
        if letters and amount:
            for letter in letters:
                bag += (build_tile_set(amount, letter))     

    return bag

def assign_tiles(bag):
    player_rack = []
    for i in range(7):
        player_rack.append(choice(bag))
    
    return player_rack
      
def load_valid_words():
    with open("./dictionary.txt", "r") as f:
        words = f.read().splitlines()
    
    return words 

def valid_words_from_rack(rack, words):
    valid_words = words
    temp_words = []
    letters = [tile["letter"].lower() for tile in rack]
    
    for letter in letters:
        for word in valid_words:
            if letter in word:
                temp_words.append(word)
        valid_words = temp_words
        temp_words = []
    

    return valid_words
            
def longest_valid_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word
            
def highest_scoring_word(words):
    highest_scoring_word = ""
    
    for word in words:
     
        if calculate_score(word.upper()) > calculate_score(highest_scoring_word.upper()):
            highest_scoring_word = word
    
    return highest_scoring_word


if __name__ == '__main__':
    #calculating score
    print(f'score for GUARDIAN: \n {calculate_score("GUARDIAN")}')
    
    #creating a rack from the alphabet
    alphabet_rack = build_rack_from_alphabet()
    print(f"alphabet_rack : \n {alphabet_rack}")
    
    #creating a a bag from the distribution and a rack from the bag 
    distribution = [
        {12:"E"},
        {9:"AI"},
        {8:"O"},
        {6:"NRT"},
        {4:"LSUD"},
        {3:"G"},
        {2:"BCMPFHVWY"},
        {1:"KJXQZ"},
    ]
    bag = build_bag(distribution)
    player_rack = assign_tiles(bag)
    print(f"player rack: \n {player_rack}")
    
    #looking for a valid words
    valid_words = load_valid_words()
    test_rack =  [
    {'letter': 'R', 'points': 1}, 
    {'letter': 'O', 'points': 1},
    {'letter': 'L', 'points': 1}, 
    {'letter': 'S', 'points': 1},
    {'letter': 'A', 'points': 1}, 
    {'letter': 'S', 'points': 1}, 
    {'letter': 'J', 'points': 8}
    ]
    player_valid_words = valid_words_from_rack(test_rack, valid_words)
    print(f"all valid words: \n {player_valid_words}")
    print(f" one word: \n {choice(player_valid_words)}")
    
    #finding the longest valid word
    print(f"longest_word: {longest_valid_word(player_valid_words)}")
    
    #finding the highest scoring word that can be formed:
    print(f" highest scoring word: {highest_scoring_word(player_valid_words)}")
    
    
    
    
    
    