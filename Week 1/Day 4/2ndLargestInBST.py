import unittest


def contains(ordered_list, number):

    # Check if an integer is present in the list
    floor_index = 0
    ceiling_index = len(ordered_list)
    
    while floor_index < ceiling_index:
        guess_index = (floor_index + ceiling_index) // 2
        guess_value = ordered_list[guess_index]
        
        
        if guess_value == number:
            return True

        if guess_value > number:
            # target is to the left
            # so move ceiling to the left
            ceiling_index = guess_index - 1

        else:
            # target is to the right
            # so move floor to the right
            floor_index = guess_index + 1

    return False


# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)
