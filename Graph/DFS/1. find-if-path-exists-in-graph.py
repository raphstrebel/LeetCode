class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Runtime: O(E) to build linked list + O(E + V) to iterate over all neighbours of all nodes (in the worst case)
                 -> O(E + V)
        Space: O(E) for linked list + O(V) vertices in the stack 
               -> O(E + V)
        """
        if source == destination:
            return True
        if len(edges) == 0:
            return False
        
        # build linked list to navigate through edges easily
        edge_dict = defaultdict(list)
        for x, y in edges:
            edge_dict[y].append(x)
            edge_dict[x].append(y)
        
        # Depth-First Search
        visited = set()
        stack = []
        # start at source, no need to iterate over all connected components
        stack.append(source)
        while len(stack) > 0:
            # retrieve first element of list
            x = stack.pop(0)
            # if the element is visited, all neighbours are in stack
            if x in visited:
                continue
            # add all neighbours of x that have not been visited
            for y in edge_dict[x]:
                if not y in visited:
                    if y == destination:
                        return True
                    stack.append(y)
            visited.add(x)
        return False