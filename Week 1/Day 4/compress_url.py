import unittest
d1={}
class Trie(object):

    def add_word(self, word):
        global d1
        cur = d1
        nwrd = False
        for i in word:
            if i not in cur:
                nwrd = True
                cur.update({i:{}})
            cur= cur[i]
        if "End Of Word" not in cur:
            nwrd = True
            cur.update({"End Of Word":{}})
        return nwrd

# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
