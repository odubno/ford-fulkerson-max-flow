def bfs(graph, source, sink):
    """ Find shortest path between source and sink if path exists.
    :param graph:
    :param source:
    :param sink:
    :return:
    """
    queue, visited = [(source, [source])], [source]
    while queue:
        u, path = queue.pop(0)
        edge_nodes = set(graph[u].keys()) - set(path)
        for v in edge_nodes:
            if v in visited:
                continue
            visited.append(v)
            if not graph.has_edge(u, v):
                continue
            elif v == sink:
                return path + [v]
            else:
                queue.append((v, path + [v]))