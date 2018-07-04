import unittest

class QueueTwoStacks(object):
    def __init__(self):
        self.firstStack=[]
        self.secondstack=[]

    def enqueue(self, item):
        while(self.firstStack!=[]):
            self.secondstack.append(self.firstStack.pop())
        self.firstStack.append(item)
        while(self.secondstack!=[]):
            self.firstStack.append(self.secondstack.pop())

    def dequeue(self):
        if(self.firstStack==[]):
            raise Exception
        else:
            return self.firstStack.pop()

# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)
