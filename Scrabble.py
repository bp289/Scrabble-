from random import choice
from string import ascii_uppercase

#task 1
def calculate_Score(word):
    points_For_Letter = {
        1: "EAIONRTLSU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ" 
    }
    if not word:
        return 0
    
    result = 0
    for letter in word:
        for x in points_For_Letter:
            if points_For_Letter[x].__contains__(letter):
                result += int(x)
        
    
    return result
print(calculate_Score("GUARDIAN"))

#task 2
Rack = ""
def assign_tiles(): 
    letters = ascii_uppercase
    for i in range(7):
        Rack += choice(letters)
print(Rack)      

#task 3
def build_Set(number, tiles):
    bag = ""
    for i in range(number):
        times+= bag
    return bag  
def build_Bag():
    bag = f"{build_Set(12, 'E')}{build_Set(9, 'AI')}{build_Set(8, 'O')}{build_Set(6, 'NRT')}{build_Set(4, 'LSUD')}{build_Set(3, 'G')}{build_Set(2, 'BCMPFHVWY')}{build_Set(1, 'KJXQZ')}"
    return bag    
def build_Rack(bag):
    rack = ""
    for i in range(7):
        rack += choice(bag)
    return 
Bag = build_Bag()
playerRack = build_Rack()

#task 4
def getWords():
    with open("dictionary.txt", "r") as f:
        words = f
    return words
def find_valid_words(rack, words):
    
    return ""
possible_words = find_valid_words(playerRack, getWords())
