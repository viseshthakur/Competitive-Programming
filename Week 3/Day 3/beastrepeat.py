import unittest

def find_duplicate(list):

    lenlist = len(list)
    list1 = lenlist
    list2 = lenlist
    while True:
        list1 = list[list1-1]
        list2 = list[list[list2-1]]
        if list1 == list2:
            break

    list2 = lenlist
    while True:
        list1 = list[list1-1]
        list2 = list[list2-1]
        if list2 == list1:
            return list1

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1,2,2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long(self):
        actual = find_duplicate([5, 1, 4, 8, 3, 2, 7, 6, 4])
        expected = 4
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)