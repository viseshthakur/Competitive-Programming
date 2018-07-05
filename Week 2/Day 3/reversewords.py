import unittest

def reverse(list_of_chars, start, end):
    limit = start + (end-start)//2
    for i in range (start,limit):
        (list_of_chars[i], list_of_chars[start+end-i-1] ) = (list_of_chars[start+end-i-1], list_of_chars[i])
    return list_of_chars

def reverse_words(word):
    word_len = len(word)
    word = reverse(word,0,word_len)
    i=0
    while(i<word_len):
        start = i
        while(i<word_len and word[i]!=' '):
            i+=1
        end = i
        word = reverse(word,start,end)
        i+=1
    return word

# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        message=reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        message=reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        message=reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        message=reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        message=reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        message=reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
