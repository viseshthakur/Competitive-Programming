import unittest

def get_permutations(input):
    ans = []
    leninput = len(input)
    if(leninput==0 or leninput==1):
        return set([input])
    for var in range (leninput):
        new = input[0:var]+input[var+1:leninput]
        lis = get_permutations(new)
        for k in lis:
            ans.append(input[var]+k)
    return set(ans)

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
