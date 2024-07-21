class Graph():
    def __init__(self, edges):
        self.edges      = edges
        self.graph_dict = {}

    def build_graph(self):
        for source, destination in self.edges:
            if source in self.graph_dict :
                self.graph_dict[source].append(destination)
            else :
                self.graph_dict[source] = [destination]
        
        return self.graph_dict

    def get_path(self, start, end):
        path = [start]
        all_paths = []
        
        if start == end :
            return [path]
        
        if start not in self.graph_dict :
            return []
        
        for node in self.graph_dict[start] :
            if node not in path :
                new_paths = (self.get_path(node, end))
            
            all_paths += new_paths

        return all_paths


if __name__ == '__main__':
    flight_routes = [
        ('Mumbai', 'Dubai'),
        ('Mumbai', 'Paris'),
        ('Paris', 'New York'),
        ('Paris', 'Frankfurt'),
        ('Dubai', 'London'),
        ('Dubai', 'New York'),
        ('London', 'Toronto')
    ]
    graph = Graph(flight_routes)
    print(graph.build_graph())

    print(graph.get_path('Mumbai', 'New York'))