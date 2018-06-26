import unittest


def merge_meets(meetings_list):
    if len(meetings_list) < 2:
        raise IndexError('Error Less than two numbers')

    sorted_meet = sorted(meetings_list)
    new_list = [sorted_meet[0]]

    for meeting_start, meeting_end in sorted_meet[1:]:
        merged_start, merged_end = new_list[-1]

        if (meeting_start <= merged_end):
            new_list[-1] = (merged_start,max(merged_end,meeting_end))
        else:
            new_list.append((meeting_start, meeting_end))

    return new_list

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_meets([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_meets([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_meets([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_meets([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_meets([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_meets([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_meets([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
