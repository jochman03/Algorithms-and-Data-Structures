import polska

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

class graph_matrix:
    def __init__(self, no_connection=0):
        self.matrix = list()
        self.vertex_ids = list()
        self.no_connection = no_connection
    def is_empty(self):
        if len(self.matrix) == 0:
            return True
        return False
    def insert_vertex(self, vertex):
        if vertex not in self.vertex_ids:
            self.vertex_ids.append(vertex)
            for row in self.matrix:
                row.append(self.no_connection)
            self.matrix.append([self.no_connection] * (len(self.vertex_ids)))
    def insert_edge(self, vertex1, vertex2, edge=1):
        vertex1_id = self.get_vertexid(vertex1)
        vertex2_id = self.get_vertexid(vertex2)
        if vertex1_id == None or vertex2_id == None:
            return None
        self.matrix[vertex1_id][vertex2_id] = edge
    def delete_vertex(self, vertex):
        vertex_id = self.get_vertexid(vertex)
        if vertex_id is None:
            return None
        self.matrix.pop(vertex_id)
        for row in self.matrix:
            row.pop(vertex_id)
        self.vertex_ids.pop(vertex_id)
    def delete_edge(self, vertex1, vertex2):
        vertex1_id = self.get_vertexid(vertex1)
        vertex2_id = self.get_vertexid(vertex2)
        if vertex1_id == None or vertex2_id == None:
            return None
        self.matrix[vertex1_id][vertex2_id] = self.no_connection

    def get_vertex(self, vertex_id):
        if vertex_id >= 0 and vertex_id < len(self.vertex_ids):
            return self.vertex_ids[vertex_id]
        return None
    
    def get_vertexid(self, vertex):
        for i in range(0, len(self.vertex_ids)):
            if self.vertex_ids[i] == vertex:
                return i
        return None
    
    def vertices(self):
        for i in range(0, len(self.vertex_ids)):
            yield i

    def neighbours(self, vertex_id):
        for i in range(0, len(self.matrix[vertex_id])):
            if self.matrix[vertex_id][i] != self.no_connection:
                yield (i, self.matrix[vertex_id][i])

def graph_coloring(graph, BFS = True):
        visited = list()
        stack = list()
        colored = dict()
        stack.append(next(graph.vertices()))
        while len(stack) > 0:
            if BFS:
                vertex = stack.pop(0)
            else:
                vertex = stack.pop()

            visited.append(vertex)
            used_colors = set()
            for n, _ in graph.neighbours(vertex):
                if f'{graph.get_vertex(n)}' in colored:
                    used_colors.add(colored[f'{graph.get_vertex(n)}'])                    
                if n not in visited and n not in stack:
                    stack.append(n)
            color = 0
            while color in used_colors:
                color += 1

            colored[f'{graph.get_vertex(vertex)}'] = color
        return list(colored.items())

def main():
    vertices = [
        'Z',
        'G',
        'P',
        'F',
        'C',
        'N',
        'W',
        'B',
        'L',
        'D',
        'E',
        'O',
        'T',
        'S',
        'R',
        'K'
    ]

    edges = [('Z','G'), ('Z', 'P'), ('Z', 'F'),
        ('G','Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
        ('N','G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
        ('B','N'), ('B', 'W'), ('B', 'L'), 
        ('F','Z'), ('F', 'P'), ('F', 'D'), 
        ('P','F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P','E'), ('P', 'O'), ('P', 'D'),        
        ('C','P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C','E'),        
        ('E','P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E','S'), ('E', 'O'),        
        ('W','C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W','T'), ('W', 'E'),        
        ('L','W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
        ('D','F'), ('D', 'P'), ('D', 'O'), 
        ('O','D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
        ('S','O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
        ('T','S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T','R'), ('T', 'K'),        
        ('K','S'), ('K', 'T'), ('K', 'R'), 
        ('R','K'), ('R', 'T'), ('R', 'L')]
    
    graph_1 = graph_matrix()

    for v in vertices:
        graph_1.insert_vertex(vertex(v))
    for e1, e2 in edges:
        graph_1.insert_edge(vertex(e1), vertex(e2))

    colors_dfs = graph_coloring(graph_1, False)
    colors_bfs = graph_coloring(graph_1, True)
    print(f"Maksymalna liczba kolorów DFS = {max(color for _, color in colors_dfs) + 1}")
    print(f"Maksymalna liczba kolorów BFS = {max(color for _, color in colors_bfs) + 1}")

    polska.draw_map(graph_1, colors_bfs)
    polska.draw_map(graph_1, colors_dfs)


if __name__ == "__main__":      
    main()  