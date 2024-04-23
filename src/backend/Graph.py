class Graph:
    def __init__(self):             # constructor
        self.edges = dict()         # dictionary format: key - edge (tuple (start, end)); elem - it's weight
        self.N = None               # the number of vertices
        self.start = None           # start vertex number
        self.paths = dict()         # dictionary of shortest paths to all the vertices
        self.config = None          # graph configuration

    def checking(self):
        counter = set()
        for key in self.edges.keys():
            counter.add(key[0])
            counter.add(key[1])
        if len(counter) != self.N:
            self.edges = dict()
            self.N = None
            self.start = None