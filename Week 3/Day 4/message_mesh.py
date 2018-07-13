import unittest

def bfs_search_to_path(graph, start, end):

    start_node = graph.setdefault(start, None)
    end_node = graph.setdefault(end, None)
    if(start_node == None or end_node == None):
        raise Exception
    visit_made = []
    parent_list = {}
    queue_of_nodes = []
    flag = False
    queue_of_nodes.append(start)
    while(len(queue_of_nodes)>0 and flag == False):
        node = queue_of_nodes.pop(0)
        if(node not in visit_made):
            visit_made.append(node)
            temp_node = graph[node]
            for x in temp_node:
                if (x!=end and x not in visit_made):
                    parent_list[x]=node
                    queue_of_nodes.append(x)
                elif(x==end):
                    queue_of_nodes.append(x)
                    parent_list[x]=node
                    flag = True
                    break
    var1 = parent_list.setdefault(end,None)
    
    if (var1 == None):
        return None
    else:
        result = []
        curr = end
        while(curr != start):
            result.append(curr)
            curr = parent_list[curr]
        result.append(curr)
        result.reverse()
        return result

# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_search_to_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_search_to_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_search_to_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_search_to_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_search_to_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_search_to_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_search_to_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_search_to_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_search_to_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)