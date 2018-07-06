import unittest

def find_repeat(listnum):

    # Find the number that appears twice
    n = len(listnum)
    for i in range (n):
        print('-----'+str(i))
        if(listnum[abs(listnum[i])] > 0) :
            listnum[abs(listnum[i])] = (-1) * listnum[abs(listnum[i])]
            print(listnum[abs(listnum[i])])
        else :
            return abs(listnum[i])

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = find_repeat([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)

    def test_list(self):
        actual = find_repeat([1,2,3,4,5,6,1])
        expected = 1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
