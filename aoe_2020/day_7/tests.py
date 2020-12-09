from solution import *
from matplotlib import pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import pytest

data = [x for x in open('test.txt').read().splitlines()]
data2 = [x for x in open('test2.txt').read().splitlines()]


def test_part_1():
    G_1 = build_graph(data)

    G = nx.DiGraph()
    G.add_edge("light red", "bright white", weight=1)
    G.add_edge("light red", "muted yellow", weight=2)

    G.add_edge("dark orange", "bright white", weight=3)
    G.add_edge("dark orange", "muted yellow", weight=4)

    G.add_edge("bright white", "shiny gold", weight=1)

    G.add_edge("muted yellow", "shiny gold", weight=2)
    G.add_edge("muted yellow", "faded blue", weight=9)
    
    G.add_edge("shiny gold", "dark olive", weight=1)
    G.add_edge("shiny gold", "vibrant plum", weight=2)
    
    G.add_edge("dark olive", "faded blue", weight=3)
    G.add_edge("dark olive", "dotted black", weight=4)
    
    G.add_edge("vibrant plum", "faded blue", weight=5)
    G.add_edge("vibrant plum", "dotted black", weight=6)


    predecessors = nx.algorithms.dag.ancestors(G_1, "shiny gold")

    # labels = nx.get_edge_attributes(G,'weight')
    # # pos = nx.spring_layout(G)
    # pos = nx.spring_layout(G, weight=None, k=1)
    # # nx.draw_networkx_nodes(G, pos)
    # # nx.draw_networkx_labels(G, pos)
    # # nx.draw_networkx_edges(G, pos)
    # nx.draw_networkx(G, pos)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # # nx.draw(G)
    # plt.show()




def test_part_2():
    G = build_graph(data)
    assert count_bags_inside(G, "shiny gold") - 1 == 32

    G = build_graph(data2)
    assert count_bags_inside(G, "shiny gold") - 1 == 126