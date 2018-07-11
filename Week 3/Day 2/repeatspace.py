import unittest

def find_repeat(arrList):

    upper = len(arrList)-1
    lower = 1
    while(lower<upper):
         middle = (lower+upper)//2
         lowlower = lower
         lowupper = middle
         uplower = middle+1
         upupper = upper
         ldist = lowupper - lowlower + 1
         count = 0
         for var1 in arrList:
             if(var1>=lowlower and var1<=lowupper):
                 count+=1
         if (count>ldist):
             lower = lowlower
             upper = lowupper
         else:
             lower = uplower
             upper = upupper
    return lower

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
