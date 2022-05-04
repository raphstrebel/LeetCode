class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Using a stack"""
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


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Using recursion"""
        n = len(graph)
        if n == 1:
            return graph
        
        target = n - 1
        paths = []
        def rec(x, path):
            # if x is the target, then this path stop here
            if x == target:
                paths.append(path[:])
                return
            # otherwise, go over all neighbours of x using the path
            for y in graph[x]:
                path.append(y)
                # try reaching target from y
                rec(y, path)
                # remove already explored path
                path.pop()

        # start from node 0, the path is just [0]
        rec(0, [0])
        return paths