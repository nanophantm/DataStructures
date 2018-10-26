'''
Vertices = {a,b,c,d,e}
Edges = {ab,ac,bd,cd,de}

a               b
o---------------o
|               |
|               |
|               |
|               |
o---------------o-----------o
c               d           e

'''
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    
    """
        getVertices()
            return the vertices of the graph
        
        All this is doing is getting the keys of the dictionary
    """
    def getVertices(self):
        return list(self.gdict.keys())
    
    """
        Return a list of edges
    """
    def findedges(self):
        edgename = []
        # Loop through the vertices in the graph
        for vrtx in self.gdict:
            # Loop through the items in the vertices connections
            for nxtvrtx in self.gdict[vrtx]:
                # If the vertice combinations arent in the list add them
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        # Return a list containing the edges
        return edgename

    """
        Add a vertex
    """
    # Pretty straiht forward. If the vertex doesnt exist in the dictionary
    # then add it.
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    
    """
        Add Edge
    """
    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


# Create the diciontary with graph elements
graph = {"a" : ["b","c"],
         "b" : ["a","d"],
         "c" : ["a","d"],
         "d" : ["e"],
         "e" : ["d"]
}


print(graph)

g = Graph(graph)
g.addVertex("f")
g.addEdge({'f','b'})
g.addEdge({'f','e'})
print(graph)
print(g.getVertices())
print(g.findedges())

'''
test_keys = {"1": "foo", "2": "bar", "3": "fra"}
just_keys = print(list(test_keys.keys()))
'''