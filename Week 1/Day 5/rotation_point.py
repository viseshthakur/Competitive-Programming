import unittest

def find_rotation_point(words):
    ind = 0
    size = len(words)
    if size > 1:
        le = 0
        ri = size - 1

        while (ri - le) > 1:
            if words[le] > words[ri]:
                nexttry = int((le + ri) / 2.0 + 0.5)
                if words[nexttry] > words[ri]:
                    le = nexttry
                else:
                    ri = nexttry
            else:
                return le

        if words[le] <= words[ri]:
            ind = le
        else:
            ind = ri

    return ind

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
