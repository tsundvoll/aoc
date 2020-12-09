import networkx as nx

data = [x for x in open('input.txt').read().splitlines()]

def build_graph(input_data):
    G = nx.DiGraph()

    for line in input_data:
        words = line.split()
        if len(words) == 7:
            continue
        
        bag_color = " ".join(words[:2])
        
        i = 4
        while i < len(words):
            number = int(words[i])
            color = " ".join(words[i+1:i+3])

            G.add_edge(bag_color, color, weight=number)
            i += 4

    return G


def count_bags_inside(G, color):
    local_sum = 1
    for node, value in G[color].items():
        local_sum += count_bags_inside(G, node)*value["weight"]
    return local_sum


def solution_part_1():
    G = build_graph(data)
    predecessors = nx.algorithms.dag.ancestors(G, "shiny gold")

    return len(predecessors)


def solution_part_2():
    G = build_graph(data)
    return count_bags_inside(G, "shiny gold") - 1


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())