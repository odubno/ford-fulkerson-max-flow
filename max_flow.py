import networkx as nx
from ford_fulkerson import ford_fulkerson


def reduce_graph(graph):
    """ Transform a bipartite graph into a directed flow network with source and sink.
    :param graph: (networkx.classes.digraph.DiGraph)
    :return:
        bipartite G -> network flow
        R(G) -> G'
    """
    G = graph.copy()
    all_nodes = G.nodes()
    G.add_node('source')
    G.add_node('sink')
    for n in all_nodes:
        demand = G.node[n]['demand']
        if demand < 0:
            G.add_edge('source', n, capacity=-demand)
        else:
            G.add_edge(n, 'sink', capacity=demand)
    return G


def calc_flow(G_f, G):
    """ Calculate the flow for each node inside of G (original graph)
    :param G_f: the residual graph Gf, after all flow has been maxed
    :param G: the original graph.
    :return:
        Use the original graph and the augmented graph to calculate flow for each node.
    """
    flow = {i: {} for i in G}
    for u, v in G.edges_iter():
        if G_f.has_edge(u, v):
            f = G[u][v]['capacity'] - G_f[u][v]['capacity']
            flow[u][v] = max(0, f)
        else:
            flow[u][v] = G[u][v]['capacity']
    return flow


def flow_with_demands(graph):
    """Computes a flow with demands over the given graph.

    Args:
        graph: A directed graph with nodes annotated with 'demand' properties and edges annotated with 'capacity'
            properties.

    Returns:
        A dict of dicts containing the flow on each edge. For instance, flow[s1][s2] should provide the flow along
        edge (s1, s2).

    Raises:
        NetworkXUnfeasible: An error is thrown if there is no flow satisfying the demands.
    """
    G = graph.copy()
    demand_satisfied = sum([G.node[i]['demand'] for i in G.nodes()]) == 0
    if not demand_satisfied:
        raise nx.NetworkXUnfeasible('An error is thrown if there is no flow satisfying the demands.')
    reduced_graph = reduce_graph(G)
    G_f = ford_fulkerson(reduced_graph, 'source', 'sink')
    flow = calc_flow(G_f, G)
    return flow


if __name__ == '__main__':
    pass