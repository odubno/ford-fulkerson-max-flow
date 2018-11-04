import pytest
import networkx as nx

from max_flow import flow_with_demands


def divergence(flow):
    """Computes the total flow into each node according to the given flow dict.

    Args:
        flow: the flow dict recording flow between nodes.

    Returns:
        A dict of the net flow into each node.
    """
    div = {k: 0 for k in flow.keys()}
    for node in flow.keys():
        forward_flow = sum(flow[node].values())
        backward_flow = sum(flow[i][node] for i in flow[node].keys())
        div[node] = backward_flow - forward_flow
    return div


def test_max_flow():
    G = nx.Graph()
    usa = open('contiguous-usa.dat')
    for i, line in enumerate(usa):
        s1, s2 = line.strip().split()
        G.add_edge(s1, s2)
    for state in G.nodes():
        if state != 'CA':
            G.node[state]['demand'] = 1
    G.node['CA']['demand'] = -48
    G = nx.DiGraph(G)
    uniform_capacity = 16
    for (s1, s2) in G.edges():
        G.edge[s1][s2]['capacity'] = uniform_capacity
    flow = flow_with_demands(G)
    div = divergence(flow)
    assert all(div[n] == G.node[n]['demand'] for n in G.nodes())


if __name__ == '__main__':
    test_max_flow()