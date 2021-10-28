from LinkedList import LinkedList


class Vertex:
    def __init__(self, vertex_name=None):
        self.edges = LinkedList()
        self.vertex_name = vertex_name


class Graph:
    def __init__(self):
        # vertex_edges - list of all corners in graph
        self.vertexes = LinkedList()
        self.length = 0
        self.vert_name_list = LinkedList()

    def insert(self, vertex_name, vertex_edges):
        print("-" * 100, "\ndef insert\n", "-" * 100)

        # check if there are elements in the vertex list
        if self.vert_name_list.lookup(vertex_name) is None:
            self._insert(vertex_name, vertex_edges)

        if self.vert_name_list.lookup(vertex_edges) is None:
            self._insert(vertex_edges, vertex_name)

        self._append(vertex_name, vertex_edges)
        self._append(vertex_edges, vertex_name)

    def _append(self, vertex, edges):
        link = self.lookup(vertex)
        link.edges.append(edges)

    def _insert(self, vertex_name, vertex_edges):
        temp = Vertex(vertex_name)
        temp.edges.append(vertex_edges)
        temp.vertex_name = vertex_name
        # append new vertex to list of vertex_edges
        self.vertexes.append(temp)
        self.vert_name_list.append(vertex_name)
        self.length += 1

    def lookup(self, vertex):
        # print(vertex)
        res = False
        self.vertexes.start = 0
        for i in range(self.vert_name_list.length):
            link = next(self.vertexes)
            if link is not None:
                if link.vertex_name == vertex:
                    res = link
        self.vertexes.start = 0
        return res

    def delete(self, vertex):
        self.vertexes.start = 0
        ind = None
        vert_ind = None
        for i in range(self.vert_name_list.length):
            link = next(self.vertexes)
            if link.vertex_name == vertex:
                vert_ind = self.vertexes.lookup(link)
            temp_ind = link.edges.lookup('a')
            if ind is not None:
                link.edges.delete(temp_ind)

        self.vertexes.delete(vert_ind)

        # delete from self.vert_name_list
        ind = self.vert_name_list.lookup(vertex)
        if ind is not None:
            self.vert_name_list.delete(ind)


# l = LinkedList()
graph = Graph()
graph.insert("a", "b")
graph.lookup("a")
graph.insert("a", "c")
graph.insert("b", "c")
graph.lookup("c")
graph.insert("f", "c")
graph.lookup("a")
graph.lookup("f")
graph.delete('a')
print(graph.vert_name_list.lookup('a'))
print(graph.lookup("a"))