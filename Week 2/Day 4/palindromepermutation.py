import unittest

def has_palindrome_permutation(input):
    lenstr = len(input)
    di = {}
    for i in range (lenstr):
        no = di.setdefault(input[i], 0)
        di[input[i]]=no+1
        
    if (lenstr%2==0):
        for var in di.keys():
            if (di[var]%2!=0):
                return False
    else:
        f = False
        for var in di.keys():
            if (di[var]%2!=0):
                if(f == True):
                    return False
                else:
                    f = True
    return True

# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
