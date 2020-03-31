# -*- coding: utf-8 -*-
"""Graph module.
Provide an implementation of graphs with adjacency lists.
In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. The vertex key, or number, can then be used to access its
adjacency list.
"""


class Graph:
    """ Simple class for graph: adjacency lists
    Attributes:
        order (int): Number of vertices.
        directed (bool): True if the graph is directed. False otherwise.
        adjlists (List[List[int]]): Lists of connected vertices for each vertex.
    """

    def __init__(self, order, directed=False):
        """Init graph, allocate adjacency lists
        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.
        """

        self.order = order
        self.directed = directed
        self.adjlists = []
        for _ in range(order):
            self.adjlists.append([])


    def addedge(self, src, dst):
        """Add egde to graph.

        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.

        Raises:
            IndexError: If any vertex index is invalid.

        """
        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")

        self.adjlists[src].append(dst)
        if not self.directed and dst != src:
            self.adjlists[dst].append(src)


    def addvertex(self, number=1):
        """Add number vertices to graph.

        Args:
            ref (Graph).
            number (int): Number of vertices to add.

        """

        # Increment order and extend adjacency list
        self.order += number
        for _ in range(number):
            self.adjlists.append([])

def todot(ref):
    """Write down dot format of graph.
    Args:
        Graph
    Returns:
        str: String storing dot format of graph.
    """

    # Check if empty graph.
    if ref is None:
        return "graph G { }"
    # Build dot for non-empty graph.
    (s, link) = ("digraph ", " -> ") if ref.directed else ("graph ", " -- ")
    s += " G {\n"
    for src in range(ref.order):
        s += str(src) + '\n'
        for dst in ref.adjlists[src]:
            if ref.directed or src >= dst:
                s += "  " + str(src) + link + str(dst) + '\n'
    s += '}'
    return s

def display(G, eng=None):
    """
    *Warning:* Made for use within IPython/Jupyter only.
    """

    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    display(Source(todot(G), engine = eng))


# load / save gra format

def loadgra(filename):
    """Build a new graph from a GRA file.
    Args:
        filename (str): File to load.
    Returns:
        Graph: New graph.
    Raises:
        FileNotFoundError: If file does not exist. 
    """

    f = open(filename)
    directed = bool(int(f.readline()))
    order = int(f.readline())
    g = Graph(order, directed)
    for line in f.readlines():
        edge = line.strip().split(' ')
        (src, dst) = (int(edge[0]), int(edge[1]))
        g.addedge(src, dst)
    f.close()
    return g

def savegra(G, fileOut):
    gra = str(int(G.directed)) + '\n'
    gra += str(G.order) + '\n'
    for s in range(G.order):
        for adj in G.adjLists[s]:
            if G.directed or s >= adj:
                gra += str(s) + " " + str(adj) + '\n'
    fout = open(fileOut, mode='w')
    fout.write(gra)
    fout.close()

