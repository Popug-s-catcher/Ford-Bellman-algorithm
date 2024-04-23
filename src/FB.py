INF = 10 ** 9


def FB_alg(N, start, graph, paths):
    F = [INF] * N
    F[start] = 0
    prev = [0] * N
    log_data = ""

    for k in range(1, N):
        log_data += "0_0 Looking for the shortest paths consisting no more than %d edge(s)\n" % (k)
        F_s = [str(i) for i in F]
        log_data = log_data + "\nF array:\n[" + ', '.join(F_s) + "]\n\n"
        for j, i in graph.keys():
            log_data += "\n> Checking edge (%d, %d) with weight [%d]\n" % (j, i, graph[j,i])
            if F[j] + graph[j, i] < F[i]:
                log_data += "\n+ Current edge is matching a minimal path condition\n" \
                            "Path until (%i) vertex has been updated by the value of [%d]\n" % (i, graph[j,i])
                F[i] = F[j] + graph[j, i]
                F_s = [str(i) for i in F]
                log_data = log_data + "\nCurrent F array:\n[" + ', '.join(F_s) + "]\n\n"
                prev[i] = j
            else:
                log_data += "\n- Edge is not matching\n\n"

    log_data += "\n\n0_0 Looking for negative cycle:\n\n"
    cycle_found = False
    for j, i in graph.keys():
        log_data += "\n> Checking edge (%d, %d) with weight [%d]\n" % (j, i, graph[j,i])
        if F[j] + graph[j, i] < F[i]:
            log_data += "! Current edge starts the negative cycle\n"
            cycle_found = True
            break
        else:
            log_data += "+ OK\n"

    text = "Start vertex [%d]\n" % (start)
    if cycle_found is True:
        text += "Graph consists negative cycle reachable from the start vertex!"
        log_data += "\nGraph consists negative cycle reachable from the start vertex!"
        return text, log_data
    else:
        log_data += "\nGraph does not consist negative cycle\n+++ Reconstructioning the paths +++\n\n"
        for i in range(N):
            j = i
            chain = [j]
            while j != start:
                if F[j] == INF:
                    break
                chain.append(prev[j])
                j = prev[j]
            chain.reverse()
            if chain[0] != start:
                F[i] = INF
                chain = [i]
            paths[i] = chain

        log_data += "\nAnswer (start vertex [%d])\nEnd-vertex\t\tDistance\t\tPath (verticies)\n" % (start)
        for i in paths.keys():
            paths_str = [str(s) for s in paths[i]]
            if F[i] == INF:
                text = text + str(i) + "\t\t" + '∞' + "\t\t" + "\n\n"
                log_data = log_data + str(i) + "\t\t" + '∞' + "\t\t" + '->'.join(paths_str) + "\n\n"
            else:
                text = text + str(i) + "\t\t" + str(F[i]) + "\t\t" + "\n\n"
                log_data = log_data + str(i) + "\t\t" + str(F[i]) + "\t\t" + '->'.join(paths_str) + "\n\n"
    return text, log_data
