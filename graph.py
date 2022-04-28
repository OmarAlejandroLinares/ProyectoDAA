import collections
import sys
from graphviz import Digraph
from graphviz import Graph as Graphviz

import edge
import vertex

# Attribute to indicate if is a directed graph
DIRECTED = "DIRECTED"

# Render images graphviz
RENDER = False

# Attribute to inidcate if a vertes has been discovered
DISCOVERED = "DISCOVERED"


class Graph:
    def __init__(self, vertices=None, edges=None, attr={}):
        """__init__ initializes Graph object. Graph stores vertices and edges
           param vertices: Dictionary with vertices
           param edges:    Dictionary with edges
           param attr:     Properties of graph
        """
        if vertices is None:
            vertices = {}
        self.vertices = vertices

        if edges is None:
            edges = {}
        self.edges = edges

        self.attr = attr

    def add_vertex(self, vertex):
        """ add_vertex add vertex to graph's vertices
            if there is not other vertex with same id
            param vertex: vertex to add in graph
        """
        if vertex.id not in self.vertices.keys():
            self.vertices[vertex.id] = vertex

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, id):
        if id in self.vertices.keys():
            return self.vertices[id]
        else:
            return None

    def add_edge(self, edge, directed=False, auto=False):
        """ Add edge to source edges
            if there is no other edge with same source and target
            :param edge: edge to insert
            :param directed: enable graph directed
            :param auto: allow auto-cycle (loops)
        """
        (v1, v2) = edge.get_id()
        if v1 in self.vertices.keys() and v2 in self.vertices.keys():
            if directed:
                if auto:
                    self.edges[edge.get_id()] = edge
                else:
                    if v1 != v2:
                        self.edges[edge.get_id()] = edge
            else:
                if self.edges.get((v2, v1)) is None:
                    if auto:
                        self.edges[edge.get_id()] = edge
                    else:
                        if v1 != v2:
                            self.edges[edge.get_id()] = edge

    def get_edges(self):
        """ edges create edges of the graph
        """
        edges = []
        for (key, target) in self.edges.keys():
            edges.append((key, target))
        return edges

    def get_edge(self, id, directed=False):
        """
        Get edge by specific id
        param id: Tupla identifier of edge
        param directed: Filter to find edge directed
        """
        (u, v) = id
        for (source, target) in self.edges.keys():
            if directed:
                if (source, target) == (u, v):
                    return self.edges[(source, target)]
            else:
                if (source, target) == (u, v) or (source, target) == (v, u):
                    return self.edges[(source, target)]
        return None

    def get_adjacent_vertices_by_vertex(self, id, type=None):
        """
        Get adjacent vertex of specific vertex
        param id: Vertex identifier in the graph
        param type: Filter
            None - All adjacent vertices
            +    - Output adjacent vertices
            -    - Input adjacent vertices
        """
        vertex = []
        for (source, target) in self.edges.keys():
            if type is None:
                if source == id:
                    vertex.append(target)
                elif target == id:
                    vertex.append(source)
            elif type == '+':
                if source == id:
                    vertex.append(target)
            elif type == '-':
                if target == id:
                    vertex.append(source)

        return vertex

    def get_edges_by_vertex(self, id, type=0):
        """
        Find the edges that are incident in vertex with id paramater
        param id: Vertex identifier in the graph
        param type: Filter output edges
            1 - Output edges
            2 - Input edges
            other - All edges
        return: list of edges
        """
        edges = []
        for (source, target) in self.edges.keys():
            if type == 1:
                if source == id:
                    edges.append((source, target))
            elif type == 2:
                if target == id:
                    edges.append((source, target))
            else:
                if source == id or target == id:
                    edges.append((source, target))
        return edges

    def clone(self):
        """
        Clone graph
        return: Clone graph
        """
        g = Graph(attr=self.attr.copy(), vertices=self.vertices.copy(),
                  edges=self.edges.copy())
        return g


    def create_graphviz(self, file_name, attr_label_vertex=None, source=None,
                        attr_label_edge=None):
        dot = Graphviz()

        # Review attribute directed of graph
        if DIRECTED in self.attr:
            if self.attr[DIRECTED]:
                dot = Digraph()
            else:
                dot = Graphviz()
        if attr_label_vertex is None:
            # Map graph to graphviz structure
            for n in list(self.vertices.keys()):
                dot.node(str(n), str(n))
        else:
            # Map graph to graphviz structure and add vertex attribute
            for n in list(self.vertices.keys()):
                label = "Node: " + str(n)
                source_label = "Node source: " + str(
                    source) if source is not None else ""
                label = label + "\n" + source_label
                label = label + "\n" + attr_label_vertex + " (" + str(
                    self.vertices[n].attributes[attr_label_vertex]) + ")"
                dot.node(str(n), label)

        if attr_label_edge is None:
            for e in self.get_edges():
                (s, t) = e
                dot.edge(str(s), str(t))
        else:
            for e in self.get_edges():
                (s, t) = e
                label_edge = self.edges[(s, t)].attr["WEIGHT"]
                dot.edge(str(s), str(t), label=str(label_edge))

        file = open("./gv/" + file_name + ".gv", "w")
        file.write(dot.source)
        file.close()
        return dot