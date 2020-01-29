# depth first pre order traversal

# accepts and adj_list as a graph
# Graphs have a root

from graph import Graph, Vertex

class NewGraph(Graph):

    def depth_first(self, root):
        visited_lst = []
        visited_lst.append(root)

        def recurse_traverse(node):
            neighbors = self.get_neighbors(node)
            print('neighbors', neighbors)
            for neighbor in neighbors:
                if neighbor[0] not in visited_lst:
                    visited_lst.append(neighbor[0])
                    print('passed-true. neighbor[0]', neighbor[0])
                    recurse_traverse(neighbor[0])
                
            return
        
        recurse_traverse(root)
        return visited_lst