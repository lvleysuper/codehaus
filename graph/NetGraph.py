# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx


def create_graph_from_adjacent_table(adjacent_table, is_digraph = True):
    """
    :param adjacent_table: 邻接表， |V|+|E|， 定点数 + 边数
        邻接表： 前V项按顺序对应着节点，每一项取值为数组下标，表示以该节点为初始节点的边的连链表以此开始
        实例[6, 7, 8, 12, 13, 4, 1, 1, 2, 4, 5, 5, 2]
        数组第一个元素为6， 代表第一个节点的链表从6开始，可知顶点数为5
        数组第二个元素为7， 代表第二个节点的链表从7开始
    :return: 返回构建好的有向图
    """
    if not adjacent_table:
        raise ValueError("Invalid adjacent_table")

    size = len(adjacent_table)
    vertex_num = adjacent_table[0] - 1

    edge_num = size - vertex_num
    if not check_vertex(adjacent_table[0 : vertex_num], size):
        raise ValueError("Invalid adjacent link address")

    if not check_vertex(adjacent_table[vertex_num:], vertex_num):
        raise ValueError("Invalid vertex number")
    # 构造图
    if is_digraph:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()
    # 添加顶点
    vertexs = [i+1 for i in range(vertex_num)]
    graph.add_nodes_from(vertexs)
    # 添加边
    distance = adjacent_table[0:vertex_num]
    # 处理最后一个顶点
    distance.append(size+1)

    distance = [distance[i+1] - distance[i] for i in range(0, len(distance) - 1)]
    for i in range(0, vertex_num):
        pos = adjacent_table[i] - 1
        for j in range(pos, pos + distance[i]):
            graph.add_edge(i+1, adjacent_table[j])
    return graph


def check_vertex(v, threshold):
    v_len = len(v)
    for i in range(v_len):
        if v[i] > threshold:
            return False
    return True


def create_graph_from_adjacent_matrix(adjacent_matrix, is_digraph=True):
    pass


if __name__ == "__main__":
    # 常用经典图
    # graph = nx.petersen_graph()
    # graph = nx.tutte_graph()
    # graph = nx.sedgewick_maze_graph()
    # graph = nx.tetrahedral_graph()
    # 全连接图
    # graph = nx.complete_graph(6)
    # graph = nx.complete_bipartite_graph(3, 5)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

