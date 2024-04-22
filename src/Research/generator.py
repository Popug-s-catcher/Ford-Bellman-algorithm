import random
import time


INF = 10 ** 9


class Graph:
    def __init__(self):
        self.edges = dict()

    def read_graph_s(self, line):
        self.edges[(line[0], line[1])] = line[2]


    def print_graph_f(self):
        f = open("graph.txt", "w")
        f.write("Edges of the graph:\nStart\tFinish\tWeight\n")
        for elem in self.edges.keys():
            f.write(str(elem[0]) + "\t\t" + str(elem[1]) + "\t\t" + str(self.edges[elem]) + "\n")
        f.write("\n")
        f.close()


def generator(v, lvl, graph):
    start_time = time.time()
    if lvl == 0:                  # N
        for i in range(v - 1):
            graph.read_graph_s([i, i + 1, random.randint(-5, 50)])
        graph.read_graph_s([0, i + 1, random.randint(-5, 50)])
    else:                # 2N
        for i in range(v - 1):
            graph.read_graph_s([i, i + 1, random.randint(-5, 50)])
            graph.read_graph_s([i + 1, i, random.randint(-5, 50)])
        graph.read_graph_s([0, i + 1, random.randint(-5, 50)])
        graph.read_graph_s([i + 1, 0, random.randint(-5, 50)])
    end_time = time.time()
    print("Number of edges {%d}" % (len(graph.edges)))
    graph.print_graph_f()
    print("Graph generating time: [%f]" % (end_time - start_time))


def FB_alg(N, start, graph_in):
    graph = graph_in
    F = [INF] * N
    prev = [0] * N
    F[start] = 0

    start_time = time.time()
    for k in range(1, N):
        for j, i in graph.keys():
            if F[j] + graph[j, i] < F[i]:
                F[i] = F[j] + graph[j, i]
                prev[i] = j

    cycle_found = False
    for j, i in graph.keys():
        if F[j] + graph[j, i] < F[i]:
            cycle_found = True
            break
    end_time = time.time()

    if cycle_found is True:
        print("Graph consists negative cycle reachable from the start vertex!")
    else:
        print("OK!")

    print("Running algorithm time: [%f]" % (end_time - start_time))


def main():
    graph = Graph()
    print("Enter the number of vertices:")
    V = int(input())  # number of vertices
    print("Enter the load level of the graph (0 - easy, 1 - medium)")
    lvl = int(input())
    generator(V, lvl, graph)
    FB_alg(V, 0, graph.edges)


if __name__ == '__main__':
    main()