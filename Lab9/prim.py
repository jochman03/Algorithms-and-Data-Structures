import graf_mst
import numpy as np


class vertex:
    def __init__(self, key, brightness=0):
        self._key = key
        self._brightness = brightness
    def __eq__(self, value):
        if self._key == value:
            return True
        return False
    def __hash__(self):
        return hash(self._key)
    def __repr__(self):
        return f"{self._key}"
    def get_color(self):
        return self._brightness
    def set_color(self, brightness):
        if -1 < brightness < 256:
            self._brightness = brightness


class graph_list:
    def __init__(self):
        self._dict = dict()
    def is_empty(self):
        if len(self._dict) == 0:
            return True
        return False
    def insert_vertex(self, vertex):
        self._dict[vertex] = {}
    def insert_edge(self, vertex1, vertex2, edge=None):
        self._dict[vertex1][vertex2] = edge
    def neighbours(self, vertex_id):
        if vertex_id in self._dict:
            for n in list(self._dict[vertex_id].items()):
                yield n
        return None
    def vertices(self):
        for v in list(self._dict.keys()):
            yield v
    def delete_vertex(self, vertex):
        for i in self.vertices():
            if i == vertex:
                self._dict.pop(i)
        for k, v in self._dict.items():
            if vertex in v:
                v.pop(vertex)
    def delete_edge(self, vertex1, vertex2):
        if vertex2 in self._dict[vertex1]:
            self._dict[vertex1].pop(vertex2)

    def get_vertex(self, vertex_id):
        return vertex_id
    

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


def prim(graph: graph_list):
    mst = graph_list()
    intree = dict()
    distance = dict()
    parent = dict()
    mst_length = 0

    for v in graph.vertices():
        intree[v] = 0
        distance[v] = np.inf
        parent[v] = None

    first_vertex = next(graph.vertices())

    mst.insert_vertex(first_vertex)
    v = first_vertex
    while(intree[v] == 0):
        intree[v] = 1
        for neighbour, weight in graph.neighbours(v):
            if distance[neighbour] > weight and intree[neighbour] == 0:
                distance[neighbour] = weight
                parent[neighbour] = v
        min_weight = np.inf
        min_vertex = None
        for vertex in graph.vertices():
            if intree[vertex] == 0 and distance[vertex] < min_weight:
                min_weight = distance[vertex]
                min_vertex = vertex
        if min_vertex == None:
            break
        
        mst.insert_vertex(min_vertex)
        mst.insert_edge(min_vertex, parent[min_vertex], distance[min_vertex])
        mst.insert_edge(parent[min_vertex], min_vertex, distance[min_vertex])
        mst_length += distance[min_vertex]
        v = min_vertex
    return mst, mst_length

def main():
    edges = graf_mst.graf
    graph_1 = graph_list()
    vertex_dict = dict()
    vertexes = list()

    for v1, v2, weight in edges:
        if v1 not in vertexes:
            vertexes.append(v1)
        if v2 not in vertexes:
            vertexes.append(v2)


    for v in vertexes:
        vertex_dict[v] = vertex(v)
        graph_1.insert_vertex(vertex_dict[v])

    for v1, v2, weight in edges:
        graph_1.insert_edge(vertex_dict[v1], vertex_dict[v2], weight)
        graph_1.insert_edge(vertex_dict[v2], vertex_dict[v1], weight)

    mst, _ = prim(graph_1)
    printGraph(mst)

if __name__ == "__main__":      
    main()  