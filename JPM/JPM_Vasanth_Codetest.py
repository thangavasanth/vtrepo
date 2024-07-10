
'''
JPM Interview Code test - Python
Name: Vasanth Thangasamy
Email: thangavasanth@gmail.com
Job ID: 210531620
Job Role: Lead Software Engineer, Markets Technology team
Date: 10-jul-2024
'''

'''
Problem 1:
    Given a long statement and a input letter, find the word which contains the most number of the given character. 
    If more than one word has the exact same number of the given letter, it should return the word with the most number 
    of total letters, if more than one words have equal number of given character and total number of characters return 
    the word that appeared first in the given statement.
    
Assumptions: Include special characters
'''

def find_word_with_most_char(statement: str, char: str) -> str:
    words = statement.split()
    max_count = 0
    result_word = ""
    
    for word in words:
        char_count = word.count(char)
        if char_count > max_count:
            max_count = char_count
            result_word = word
        elif char_count == max_count:
            if len(word) > len(result_word):
                result_word = word
            elif len(word) == len(result_word) and result_word == "":
                result_word = word
            
    return result_word

'''
Problem 2:
    Write a function that accept a number and returns the starting position of the longest continuous sequence of 1s in its binary format.
Assumptions: if no 1s in the binary representation, the function returns 0
'''
def longest_sequence_of_ones_position(n: int) -> int:
    binary_representation = bin(n)[2:]
    max_len = 0
    max_pos = -1
    current_len = 0
    current_pos = 0
    #print(binary_representation)
    for i, bit in enumerate(binary_representation):
        if bit == '1':
            if current_len == 0:
                current_pos = i
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_pos = current_pos
            current_len = 0

    if current_len > max_len:
        max_len = current_len
        max_pos = current_pos
   
    return max_pos+1

# Unit Tests
import unittest

class TestFunctions(unittest.TestCase):
    
    '''
    Problem 1 Testcase
    statementJPM: This is a very long sentence and I want to educate everyone in this whole crazy world
    statement_with_special_char = Dear JPM Recruitment Team, I'm excited about this role. My email is thangavasanth@gmail.com; The project's code repository can be accessed at https://github.com/thangavasanth/vtrepo.git. let me know your feedback. 
    '''
    def setUp(self):
        self.statementJPM = "This is a very long sentence and I want to educate everyone in this whole crazy world"
        self.statement_with_special_char = "Dear JPM Recruitment Team, I'm excited about this role. My email is thangavasanth@gmail.com; The project's code repository can be accessed at https://github.com/thangavasanth/vtrepo.git. let me know your feedback. "
    def test_find_word_with_most_char_case_1(self):
        #Input character: z
        #Expected result: crazy
        self.assertEqual(find_word_with_most_char(self.statementJPM, 'z'), 'crazy')
    def test_find_word_with_most_char_case_2(self):
        #Input character: I
        #Expected result: I
        self.assertEqual(find_word_with_most_char(self.statementJPM, 'I'), 'I')
    def test_find_word_with_most_char_case_3(self):
        #Input character: e
        #Expected result: sentence
        self.assertEqual(find_word_with_most_char(self.statementJPM, 'e'), 'sentence')

    def test_find_word_with_most_char_case_4(self):
        self.statementJPM = "This is a very long and I want to educate everyone in this whole crazy world" 
        #removed word sentence from statement
        #Input character: e
        #Expected result: everyone
        self.assertEqual(find_word_with_most_char(self.statementJPM, 'e'), 'everyone')

    '''
    Problem 1 Testcase:
    statement_with_special_char = Dear JPM Recruitment Team, I'm excited about this role. My email is thangavasanth@gmail.com; The project's code repository can be accessed at https://github.com/thangavasanth/vtrepo.git. let me know your feedback. 
    '''
    def test_find_word_with_most_char_case_5(self):
        #Input character: @
        #Expected result: thangavasanth@gmail.com;
        self.assertEqual(find_word_with_most_char(self.statement_with_special_char, '@'), 'thangavasanth@gmail.com;')
    def test_find_word_with_most_char_case_6(self):
        #Input character: ,
        #Expected result: Team,
        self.assertEqual(find_word_with_most_char(self.statement_with_special_char, ','), 'Team,')
    def test_find_word_with_most_char_case_7(self):
        #Input character: /
        #Expected result: https://github.com/thangavasanth/vtrepo.git.
        self.assertEqual(find_word_with_most_char(self.statement_with_special_char, '/'), 'https://github.com/thangavasanth/vtrepo.git.')

    '''
    Problem 2 Testcases
    '''    
    def test_longest_sequence_of_ones_position_case_1(self):
        self.assertEqual(longest_sequence_of_ones_position(156), 4) # Binary: 10011100
    
    def test_longest_sequence_of_ones_position_case_2(self):
        self.assertEqual(longest_sequence_of_ones_position(88), 3) # Binary: 1011000
    
    def test_longest_sequence_of_ones_position_case_3(self):
        self.assertEqual(longest_sequence_of_ones_position(15), 1) # Binary: 1111
    
    def test_longest_sequence_of_ones_position_case_4(self):
        self.assertEqual(longest_sequence_of_ones_position(0), 0) # Binary: 0
        
        
    

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
