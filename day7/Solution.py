from collections import deque, namedtuple
import re

Edge = namedtuple('Edge', ['from_val', 'to_val'])


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.child_list = []
        self.child_map = {}
        self.num_dependency = 0

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def has_child(self, node):
        return node.val in self.child_map

    def remove_child(self, child):
        index = self.child_list.index(child)
        self.child_list.pop(index)
        del self.child_map[child.val]
        self.num_dependency -= 1

    def add_child(self, child_node):
        self.child_list.append(child_node)
        self.child_map[child_node.val] = child_node
        self.num_dependency += 1


class Graph:
    def __init__(self):
        self.node_list = []
        self.node_map = {}

    def add(self, val):
        new_node = GraphNode(val=val)
        self.node_list.append(new_node)
        self.node_map[val] = new_node
        return new_node

    def get_or_create(self, val):
        if val in self.node_map:
            return self.node_map[val]

        return self.add(val)

    def mark_node(self, child):
        for node in self.node_list:
            if node.has_child(child):
                node.remove_child(child)

    def get_topological_order(self):
        ret = []
        nodes = list(self.node_list)
        done = False

        while done == False:
            done = True

            node_to_mark = None
            mark_index = None
            for i in range(len(nodes)):
                node = nodes[i]

                if node is None:
                    continue

                if node.num_dependency == 0:
                    if node_to_mark is None:
                        node_to_mark = node
                        mark_index = i
                    else:
                        if node_to_mark.val > node.val:
                            node_to_mark = node
                            mark_index = i

            # if found node to be mark
            if node_to_mark is not None:
                ret.append(node_to_mark.val)
                self.mark_node(node_to_mark)
                nodes[mark_index] = None
                done = False

        return ret

    def add_edge(self, edge):
        from_node = self.get_or_create(edge.from_val)
        to_node = self.get_or_create(edge.to_val)
        to_node.add_child(from_node)

    def __str__(self):
        return str(self.node_list)

    def __repr__(self):
        return str(self.node_list)


class Solution:

    @classmethod
    def load_edges(cls):
        edges = []
        with open('day7/input/dependencies.txt', 'r') as in_file:
            lines = in_file.readlines()
            for line in lines:
                from_val, to_val = re.findall(r"\b[A-Z]\b", line)
                new_edge = Edge(
                    from_val=from_val,
                    to_val=to_val
                )
                edges.append(new_edge)
        return edges

    @classmethod
    def question_1(cls):
        my_graph = Graph()
        edges = cls.load_edges()
        for edge in edges:
            my_graph.add_edge(edge)

        build_order = my_graph.get_topological_order()
        print(''.join(build_order))
