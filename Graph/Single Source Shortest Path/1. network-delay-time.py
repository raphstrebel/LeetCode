class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Using Dijkstra's algorithm.
        Time complexity: O(E*log(N) + N)
            - Build adj list of graph: O(E)
            - Dijkstra: O(E*log(N)):
                - At most E edges in queue -> push/pop take O(log(E))
                - E < N^2, so log(E) < 2*log(N) -> push/pop take O(log(N))
                - Each node is visited once since we sort by increasing weight
                  and update the queue only when dist array is updated.
                -> all edges are traversed, and at each edge we do a constant
                   amount of push/pop queue operations
        Space complexity: O(N + E):
            - graph: O(E)
            - dist array: O(N)
            - queue: at most E, so O(E)
        """
        # nodes are labeled 1 to N, should be 0 to N-1
        k -= 1
        
        # build graph as adj list (change node number to correspond to index)
        graph = defaultdict(list)
        for edge in times:
            source, target, weight = edge
            graph[source-1].append((weight, target-1))
        # not all nodes are present in graph: some are unreachable
        if n < max(graph.keys()):
            return -1
        
        for node in graph:
            graph[node] = sorted(graph[node])
        # Keep track of minimum distance from source to any node
        # as well as previous node used to reach it
        # if source has no edge, target is not reachable
        if k not in graph.keys():
            return -1
        
        # initialize variables
        dist = [101] * n
        dist[k] = 0
        weight_queue = [(k, 0)]
        # run Dijkstra
        while weight_queue:
            source, path_weight = weight_queue.pop(0)
            # check if current path to source is longer
            # or if current source has no outgoing edge
            if path_weight > dist[source] or not source in graph:
                continue
            for neigh_weight, neighbor in graph[source]:
                if path_weight + neigh_weight < dist[neighbor]:
                    dist[neighbor] = path_weight + neigh_weight
                    weight_queue.append((neighbor, dist[neighbor]))
        # return maximum time to reach any node
        max_weight = max(dist)
        return -1 if max_weight == 101 else max_weight
