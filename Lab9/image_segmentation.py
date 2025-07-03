import graf_mst
import numpy as np
import cv2

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
    def get_key(self):
        return self._key

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

def graph_coloring(graph, first_vertex, color):
        visited = list()
        stack = list()
        stack.append(first_vertex)
        while len(stack) > 0:
            vertex = stack.pop()

            visited.append(vertex)
            vertex.set_color(color)
            for n, _ in graph.neighbours(vertex):                 
                if n not in visited and n not in stack:
                    stack.append(n)

        return

def image_segmentation(src):
    graph = graph_list()
    I = cv2.imread(src,cv2.IMREAD_GRAYSCALE)
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1,-1), (1, 0), (1, 1)]
    vertices = dict()

    YY = I.shape[0]
    XX = I.shape[1]
    for i in range(1, XX - 1):
        for j in range(1, YY - 1):
            vertex_id = XX * j + i
            verte = vertex(vertex_id, I[j, i])
            graph.insert_vertex(verte)
            vertices[vertex_id] = verte

    for i in range(1, XX - 1):
        for j in range(1, YY - 1):
            vertex1_id = XX * j + i
            vertex1 = vertices[vertex1_id]
            for ii, jj in neighbours:
                neighbour_i = i + ii
                neighbour_j = j + jj
                if 1 <= neighbour_j < YY - 1 and 1 <= neighbour_i < XX - 1:
                    neighbour_id = XX * neighbour_j + neighbour_i
                    neighbour = vertices[neighbour_id]
                    weight = abs(int(I[j][i]) - int(I[neighbour_j][neighbour_i]))
                    graph.insert_edge(vertex1, neighbour, weight)
    mst, _ = prim(graph)
    max_weight = -1
    max_vertex1 = None
    max_vertex2 = None

    for v in mst.vertices():
        for n, i_weight in mst.neighbours(v):
            if i_weight > max_weight:
                max_weight = i_weight
                max_vertex1 = v
                max_vertex2 = n
    mst.delete_edge(max_vertex1, max_vertex2)
    mst.delete_edge(max_vertex2, max_vertex1)

    IS = np.zeros((YY,XX),dtype='uint8')
    graph_coloring(mst, max_vertex1, 100)
    graph_coloring(mst, max_vertex2, 200)
    for v in mst.vertices():
        key = v.get_key()
        y =  key // XX
        x = key % XX
        IS[y, x] = v.get_color()
    cv2.imshow("Wynik",IS)
    cv2.waitKey()
def main():
    image_segmentation('sample.png')      


if __name__ == "__main__":
    main()