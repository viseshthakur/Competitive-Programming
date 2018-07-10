import unittest

def is_single_riffle(half1, half2, shuffled_deck):

    len_deck = len (shuffled_deck)
    len1 = len(half1)
    len2 = len(half2)
    var1 = 0
    var2 = 0
    for var3 in range (len_deck):
        if(var1<len1 and shuffled_deck[var3] == half1[var1]):
            var1+=1
        elif(var2<len2 and shuffled_deck[var3] == half2[var2]):
            var2+=1
        else:
            return False
    return True

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
