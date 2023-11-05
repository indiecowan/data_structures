'''Bi-directional graph implementation
    Indie Cowan 2023'''
import unittest

# i would like to have an adjacency matrix representation and a adjacency list representation and be able to convert between them...

class BDGraph:
    '''Bi-Directional graph implemented via adjacency matrix, values default to None'''
    def __init__(self, nodecount):
        self.nodecount = nodecount
        self.values = [None] * nodecount
        self.edges = [[0]*nodecount for i in range(nodecount)]

    # 

class test_BDGraph(unittest.TestCase):
    '''To test BDGraph'''
    def setUp(self):
        self.nodecount = 6
        self.graph = BDGraph(self.nodecount)

    def test__init__(self):
        graph = self.graph

        # test nodecount is correct
        self.assertEqual(graph.nodecount, self.nodecount)

        # test size of values
        self.assertEqual(len(graph.values), self.nodecount)

        # test values in values
        for value in graph.values:
            self.assertTrue(value is None)

        # test size of edges
        self.assertTrue(len(graph.edges), self.nodecount)
        for row in graph.edges:
            self.assertEqual(len(row), self.nodecount)
            for cell in row:
                # test all 0s in edges
                self.assertEqual(cell, 0)
        
    def test_add_

    def test_add_edge(self):
        graph = self.graph

        graph.add_edge(1, 2, 1)
        self.assertEqual(graph.edges[1][2], 1)

unittest.main()  