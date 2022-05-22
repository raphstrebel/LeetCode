class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Using queue"""
        n = len(graph)
        if n <= 1:
            return graph
        
        target = n - 1
        paths = []
        
        # source is node 0
        path = [0]
        queue = [path]
        while queue:
            # pop first path in queue
            curr_path = queue.pop(0)
            curr_node = curr_path[-1]
            # go over all neighbors of last node in path (graph is DAG)
            for next_node in graph[curr_node]:
                curr_path_copy = curr_path.copy()
                curr_path_copy.append(next_node)
                
                if next_node == target:
                    # neighbor is target, so curr_path is added to list of all paths
                    paths.append(curr_path_copy)
                else:
                    # append curr_path to queue, all neighbors will be checked later
                    queue.append(curr_path_copy)
        return paths