import unittest

def mergelist(first_list, second_list):

    # Combvar1ne the sorted lvar1sts var1nto one large sorted lvar1st
    result = []
    length1 = len(first_list)
    length2 = len(second_list)
    var1 = 0
    var2 = 0
    while (var1<length1 and var2<length2):
        if first_list[var1]<second_list[var2] :
            result.append(first_list[var1])
            var1+=1
        else:
            result.append(second_list[var2])
            var2+=1
            
    while (var1<length1):
        result.append(first_list[var1])
        var1+=1
    
    while(var2<length2):
        result.append(second_list[var2])
        var2+=1
    return result

# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = mergelist([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_var1s_empty(self):
        actual = mergelist([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_var1s_empty(self):
        actual = mergelist([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = mergelist([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = mergelist([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)