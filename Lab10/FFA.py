class vertex:
    def __init__(self, key):
        self._key = key
    def __eq__(self, value):
        if self._key == value:
            return True
        return False
    def __hash__(self):
        return hash(self._key)
    def __repr__(self):
        return f"{self._key}"

class edge:
    def __init__(self, capacity, residual = False):
        self.residual = residual
        self.residual_capacity = capacity
        self.flow = 0
        self.capacity = capacity        
    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual_capacity} {self.residual}"
    def get_capacity(self):
        return self.capacity
    def get_flow(self):
        return self.flow
    def get_residualCapacity(self):
        return self.residual_capacity
    def set_capacity(self, capacity):
        self.capacity = capacity
    def set_flow(self, flow):
        self.flow = flow
    def set_residualCapacity(self, residual_capacity):
        self.residual_capacity = residual_capacity
    def is_residual(self):
        return self.residual  
     
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
    def get_edge(self, vertex1_id, vertex2_id):
        return self._dict[vertex(vertex1_id)][vertex(vertex2_id)]

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def breadth_search(graph, start_vertex):
    visited = set()
    parent = dict()
    queue = [start_vertex]

    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            for neighbor, e in graph.neighbours(v):
                if (neighbor not in visited) and (e.get_residualCapacity() > 0):
                    parent[neighbor] = v
                    queue.append(neighbor)
    return parent

def min_capacity(graph, vertex_start, vertex_end, parent):
    min_residual_capacity = float('inf')
    v = vertex_end
    if v not in parent.keys():
        return 0
    
    while(v != vertex_start):
        e = graph.get_edge(parent[v], v)
        if e.get_residualCapacity() < min_residual_capacity:
            min_residual_capacity = e.get_residualCapacity()
        v = parent[v]

    return min_residual_capacity

def augmentation(graph, vertex_start, vertex_end, parent, min_capacity):
    v = vertex_end
    if v not in parent:
        return 0

    while v != vertex_start:
        u = parent[v]
        e_forward = graph.get_edge(u, v) 
        e_backward = graph.get_edge(v, u)

        if not e_forward.is_residual():
            e_forward.set_flow(e_forward.get_flow() + min_capacity)
        else:
            e_backward.set_flow(e_backward.get_flow() - min_capacity)

        e_forward.set_residualCapacity(e_forward.get_residualCapacity() - min_capacity)
        e_backward.set_residualCapacity(e_backward.get_residualCapacity() + min_capacity)

        v = u

def create_graph(init_graph):
    vertices = list()
    edges = list()
    graph = graph_list()
    for vertex1, vertex2, capacity in init_graph:
        if vertex1 not in vertices:
            vertices.append(vertex1)
        if vertex2 not in vertices:
            vertices.append(vertex2)
        if (vertex1, vertex2, capacity) not in edges:
            edges.append((vertex1, vertex2, capacity))
    for v in vertices:
        graph.insert_vertex(vertex(v))
    for vertex1, vertex2, capacity in edges:
        graph.insert_edge(vertex(vertex1), vertex(vertex2), edge(capacity, False))
        graph.insert_edge(vertex(vertex2), vertex(vertex1), edge(0, True))
    return graph

def actual_flow(graph, label):
    v = vertex(label)
    total = 0
    for neighbor, e in graph.neighbours(v):
        if not e.is_residual():
            total += e.get_flow()
    return total

def FFA(graph, start_label, end_label):
    vertex_start = vertex(start_label)
    vertex_end = vertex(end_label)
    max_flow = 0

    while True:
        parent = breadth_search(graph, vertex_start)
        flow = min_capacity(graph, vertex_start, vertex_end, parent)
        if flow == 0:
            break
        augmentation(graph, vertex_start, vertex_end, parent, flow)
        max_flow += flow

    return max_flow

def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graph = create_graph(graf_0)
    max_flow = FFA(graph, "s", "t")
    print(max_flow)
    printGraph(graph)
    print(actual_flow(graph, "u"))

    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graph = create_graph(graf_1)
    max_flow = FFA(graph, "s", "t")
    print(max_flow)
    printGraph(graph)
    print(actual_flow(graph, "a"))

    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graph = create_graph(graf_2)
    max_flow = FFA(graph, "s", "t")
    print(max_flow)
    printGraph(graph)
    print(actual_flow(graph, "a"))

    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]
    graph = create_graph(graf_3)
    max_flow = FFA(graph, "s", "t")
    print(max_flow)
    printGraph(graph)
    print(actual_flow(graph, "a"))

if __name__ == "__main__":      
    main()  