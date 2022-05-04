class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """DFS using a stack"""
        n = len(graph)
        if n == 1:
            return graph
        
        target = n - 1
        paths = []
        visited = set()
        # initialize the stack to be all neighbours of 0, with the path [0]
        stack = []
        for x in graph[0]:
            stack.append((x, [0]))
        while stack:
            x, path = stack.pop(0)
            if x in visited:
                continue
            # need deep copies of paths or they will be modified in place
            new_path = path[:]
            new_path.append(x)
            if x == target:
                paths.append(new_path)
            else:
                # add all neighbours of x with their path to stack
                for y in graph[x]:
                    stack.append((y, new_path))
        return paths