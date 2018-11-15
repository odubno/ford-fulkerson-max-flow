# Ford Fulkerson Max Flow

### Python code from scratch for taking a bipartite graph, reducing it to a max flow graph and finding the maximum flow for the graph.

Make sure that you're using `networkx==1.9`. See requirements.

#### The goal here is:
**Bipartite Graph** -> **Directed Flow Network** -> **Maximum Flow**
1. Reduce the **Bipartite Graph** to a **Directed Flow Network** by adding a source and a sink and introduce capacity to each. 
2. Use the Ford Fulkerson method and Breadth For Search to find augmenting paths and calculate the residual graph.
3. Using the residual graph, calculate the **Maximum Flow** for the original graph.

#### Why did I write this:
* This was a home work assignment for CSORW4246, an Algorithms course at Columbia.

## Resources:
- https://brilliant.org/wiki/ford-fulkerson-algorithm/
- https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
- https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
