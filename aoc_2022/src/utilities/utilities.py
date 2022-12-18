import matplotlib.pyplot as plt
import networkx as nx


def draf_graph(graph):
    pos = nx.spring_layout(graph, seed=225)  # Seed for reproducible layout
    nx.draw(graph, pos, with_labels=True)
    plt.show()


def graph_example():
    G = nx.Graph()
    G.add_node("A", weight=1)
    G.add_edge("A", "B")

    print(G.nodes["A"])


if __name__ == "__main__":
    graph_example()
