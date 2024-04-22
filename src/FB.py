INF = 10 ** 9                   # const value; equivalent to infinity


def FB_alg(N, start, graph, paths):          # Ford-Bellman algorithm
    F = [INF] * N             # the lengths array of the shortest paths to each vertex; all elements are INF by default
    F[start] = 0                        # except the start vertex
    prev = [0] * N                      # array to restore paths
    log_data = ""                       # logging algorithm's work

    for k in range(1, N):               # going through the paths consisting fom 1 edge until N - 1
        log_data += "0_0 Looking for the shortest paths consisting no more than %d edge(s)\n" % (k)     # logging
        F_s = [str(i) for i in F]
        log_data = log_data + "\nF array:\n[" + ', '.join(F_s) + "]\n\n"
        for j, i in graph.keys():       # looking the (j, i) edge in graph
            log_data += "\n> Checking edge (%d, %d) with weight [%d]\n" % (j, i, graph[j,i])
            if F[j] + graph[j, i] < F[i]:   # trying to find the shortest path until [i] by adding (j, i) to F[j]
                log_data += "\n+ Current edge is matching a minimal path condition\n" \
                            "Path until (%i) vertex has been updated by the value of [%d]\n" % (i, graph[j,i])
                F[i] = F[j] + graph[j, i]       # in case if it is shorter than it was, writing new F[i] value
                F_s = [str(i) for i in F]       # logging
                log_data = log_data + "\nCurrent F array:\n[" + ', '.join(F_s) + "]\n\n"
                prev[i] = j                     # rewrite the previous for [i] vertex
            else:
                log_data += "\n- Edge is not matching\n\n"  # otherwise logging about discrepancy

    log_data += "\n\n0_0 Looking for negative cycle:\n\n"   # logging
    cycle_found = False             # checking for the negative cycle
    for j, i in graph.keys():       # run one more cycle with the same algo through all the edges
        log_data += "\n> Checking edge (%d, %d) with weight [%d]\n" % (j, i, graph[j,i])
        if F[j] + graph[j, i] < F[i]:       # if algo can get the shorter path,
            log_data += "! Current edge starts the negative cycle\n"
            cycle_found = True              # than it's achieve the negative cycle
            break
        else:
            log_data += "+ OK\n"            # logging 'OK' otherwise

    text = "Start vertex [%d]\n" % (start)  # getting info to output the answer in main window
    if cycle_found is True:         # returning from the algo in case of negative cycle
        text += "Graph consists negative cycle reachable from the start vertex!"
        log_data += "\nGraph consists negative cycle reachable from the start vertex!"
        return text, log_data       # and getting data
    else:                           # otherwise
        log_data += "\nGraph does not consist negative cycle\n+++ Reconstructioning the paths +++\n\n"
        for i in range(N):              # reconstructing the paths via the prev[] array
            j = i
            chain = [j]
            while j != start:
                if F[j] == INF:
                    break
                chain.append(prev[j])
                j = prev[j]
            chain.reverse()
            if chain[0] != start:       # checking the ability to achieve the start vertex
                F[i] = INF              # in case of inability returning INF for correct answer printing
                chain = [i]
            paths[i] = chain            # and saving it to paths()

        log_data += "\nAnswer (start vertex [%d])\nEnd-vertex\t\tDistance\t\tPath (verticies)\n" % (start)
        for i in paths.keys():          # getting data
            paths_str = [str(s) for s in paths[i]]
            if F[i] == INF:
                text = text + str(i) + "\t\t" + '∞' + "\t\t" + "\n\n"
                log_data = log_data + str(i) + "\t\t" + '∞' + "\t\t" + '->'.join(paths_str) + "\n\n"
            else:
                text = text + str(i) + "\t\t" + str(F[i]) + "\t\t" + "\n\n"
                log_data = log_data + str(i) + "\t\t" + str(F[i]) + "\t\t" + '->'.join(paths_str) + "\n\n"
    return text, log_data               # and returning
