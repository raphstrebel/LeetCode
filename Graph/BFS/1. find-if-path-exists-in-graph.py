class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        if len(edges) == 0:
            return False
        
        # build linked list to navigate through edges easily
        edge_dict = defaultdict(list)
        for x, y in edges:
            edge_dict[y].append(x)
            edge_dict[x].append(y)
        
        # Breadth-First Search
        visited = set()
        queue = []
        # start at source, no need to iterate over all connected components
        queue.append(source)
        while len(queue) > 0:
            # retrieve last element of queue
            x = queue.pop()
            # if the element is visited, all neighbours are in stack
            if x in visited:
                continue
            # add all neighbours of x that have not been visited
            for y in edge_dict[x]:
                if not y in visited:
                    if y == destination:
                        return True
                    queue.append(y)
            visited.add(x)
        return False