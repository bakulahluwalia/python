'''
PROGRAMMER: Bakul Ahluwalia
ALGORITHM: Set file = "CROSSWD.txt". Set my_rack = get_input().
             
	       get_input(): Prompt user to enter scrabble rack. While
               their entry does not consist of only 7 letters: Prompt
               the user that they must only enter 7 letters and get
               input again, and set to rack. Return rack as a list
               and with each letter converted to lowercase.

           Set wordList = make_List(file).

               make_List(file): Open file. Return a list containing each
               word in the file. Close file.

           For each word in WordList: if the word is a subset of the rack
           and isValid(word, rack): set scores = (get_score(word), word).
           Store these tuples in a list, tuple or use a generator.

               get_score(word): Define a dictionary for each letter and its
               respective score. Return the sum of the scores for each character
               in word.

               isValid(word, rack): Set word_cnt = count_chars(word). Set
               rack_cnt = count_chars(rack). For all words in wordList: If the
               character count for each character in word is less than or equal
               to the character count for each character in rack: Return True.
			   Else: Return False.

               count_chars(word): Create empty dictionary called count. For each
               character in word: if character not in count: set count[ch] = 0.
               Else: set count[ch] = count[ch] + 1. Return count.

           Print each score and it's corresponding word, with the scores sorted from
		   greatest to least.
'''

file = "words.txt"

def main():
	my_rack = get_Input()
	wordList = make_List(file)
	# This generator expression creates tuples containing score and word for each word in wordList if the word is a subset 
	# of the rack and the word is a valid word (No repeated characters in word that are not in rack).
	scores = ((get_score(word), word) for word in wordList if set(word).issubset(set(my_rack)) and isValid(word, my_rack))
	display_results(scores)
	

def get_Input():
	rack = input("Enter your scrabble rack: ")
	while len(rack) != 7 or not rack.isalpha():
		print("Your rack must contain only 7 letters.")
		print()
		rack = input("Enter another scrabble rack: ")
	return list(rack.lower())

def make_List(file):
	try:
		with open(file) as f:
			return [word.strip() for word in f]
	except IOError:
		print('Error. File not found.')
	
def count_chars(word):
        count = {}
        for ch in word:
                if ch not in count:
                        count[ch] = 0
                else:
                        count[ch] += 1
        return count

def isValid(word, rack):
        word_cnt = count_chars(word)
        rack_cnt = count_chars(rack)
        # Returns True if the count for each character in word is less than or equal 
        # to the count for each character in rack. False otherwise.
        return all([word_cnt[ch] <= rack_cnt[ch] for ch in word])
       


def get_score(word):
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, 
			  "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
	return sum([scores[ch] for ch in word])

def display_results(scores):
	for score, word in sorted(scores, reverse=True):
		print(str(score)+"\t"+word)


main()
