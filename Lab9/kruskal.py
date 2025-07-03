import graf_mst

class vertex:
    def __init__(self, key, brightness=0):
        self._key = key
        self._brightness = brightness
    def __eq__(self, value):
        return self._key == value
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
    def length(self):
        return len(self._dict)
    def is_empty(self):
        return len(self._dict) == 0
    def insert_vertex(self, vertex):
        self._dict[vertex] = {}
    def insert_edge(self, vertex1, vertex2, edge=None):
        self._dict[vertex1][vertex2] = edge
    def neighbours(self, vertex_id):
        if vertex_id in self._dict:
            for n in list(self._dict[vertex_id].items()):
                yield n
    def vertices(self):
        for v in self._dict.keys():
            yield v
    def delete_vertex(self, vertex):
        self._dict.pop(vertex, None)
        for k in self._dict:
            self._dict[k].pop(vertex, None)
    def delete_edge(self, vertex1, vertex2):
        if vertex2 in self._dict.get(vertex1, {}):
            self._dict[vertex1].pop(vertex2)
    def get_vertex(self, vertex_id):
        return vertex_id
    def get_edges(self):
        edges = set()
        for u in self.vertices():
            for v, w in self.neighbours(u):
                if (v, u, w) not in edges:
                    edges.add((u, v, w))
        return list(edges)
    
class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.size = [1] * n

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def union_sets(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            if self.size[a_root] < self.size[b_root]:
                a_root, b_root = b_root, a_root
            self.p[b_root] = a_root
            self.size[a_root] += self.size[b_root]

    def same_component(self, a, b):
        return self.find(a) == self.find(b)

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def kruskal(graph):
    edges = graph.get_edges()
    edges.sort(key=lambda x: x[2])

    vert_list = list(graph.vertices())
    label_to_index = {v: i for i, v in enumerate(vert_list)}
    uf = UnionFind(len(vert_list))
    
    mst_graph = graph_list()

    for v in vert_list:
        mst_graph.insert_vertex(v)

    for u, v, w in edges:
        idx_u = label_to_index[u]
        idx_v = label_to_index[v]
        if not uf.same_component(idx_u, idx_v):
            uf.union_sets(idx_u, idx_v)
            mst_graph.insert_edge(u, v, w)
            mst_graph.insert_edge(v, u, w)

    return mst_graph

def main():
    graph = graph_list()
    vertices = set()
    for u, v, _ in graf_mst.graf:
        vertices.add(u)
        vertices.add(v)

    v_map = {}
    for v in sorted(vertices):
        vert = vertex(v)
        graph.insert_vertex(vert)
        v_map[v] = vert

    for u, v, w in graf_mst.graf:
        graph.insert_edge(v_map[u], v_map[v], w)
        graph.insert_edge(v_map[v], v_map[u], w)

    mst = kruskal(graph)
    printGraph(mst)

if __name__ == "__main__":      
    main()  
