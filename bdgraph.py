'''Bi-directional graph implementation
    Indie Cowan 2023'''
import unittest

# i would like to have an adjacency matrix representation and a adjacency list representation and be able to convert between them...

class BDGraph:
    '''Bi-Directional graph implemented via adjacency matrix'''
    def __init__(self, nodecount):
        self.nodecount = nodecount
        self.matrix = [[0]*nodecount for i in range(nodecount)]

class test_BDGraph(unittest.TestCase):
    '''To test BDGraph'''
    def setUp(self):
        self.nodecount = 6
        self.graph = BDGraph(self.nodecount)

    def test__init__(self):
        graph = self.graph
        # test nodecount is correct
        self.assertEqual(graph.nodecount, self.nodecount)

        # test size
        self.assertTrue(len(graph.matrix), self.nodecount)
        for row in graph.matrix:
            self.assertEqual(len(row), self.nodecount)
            for cell in row:
                # test all 0s
                self.assertEqual(cell, 0)

    