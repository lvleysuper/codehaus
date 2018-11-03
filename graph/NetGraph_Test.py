# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx
import unittest

from graph import NetGraph


class TestNetGraph(unittest.TestCase):

    def test_digraph_create(self):
        graph = NetGraph.create_graph_from_adjacent_table([6, 7, 8, 12, 13, 4, 1, 1, 2, 4, 5, 5, 2], is_digraph=True)
        self.assertIsNotNone(graph)
        # TODO: 添加有向图相关测试
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()

    def test_graph_create(self):
        graph = NetGraph.create_graph_from_adjacent_table([5, 7, 8, 9, 2, 3, 3, 4, 1, 2], is_digraph=False)
        self.assertIsNotNone(graph)
        #TODO: 添加无向图相关测试
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()
