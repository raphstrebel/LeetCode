class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Time: O(E) to go over all edges in recursive DFS
        Space: O(V + E): O(V) to store all vertices with paths to destination + O(E) to store recursion stack + O(E) to store adjacency list
        """
        # base cases
        if len(edges) == 0:
            return source == destination
        if source == destination:
            return False

        # build adjacency list of nodes to neighbors (ignore parallel edges)
        neighbors = defaultdict(set)
        for src, dest in edges:
            neighbors[src].add(dest)
        
        # keep track of vertices with a path to destination
        has_path = set([destination])
        def dfs(src):
            # differenciate cases where current node is destination or not
            # (destination must only have edges to nodes where it can be reached again)
            if src != destination:
                # we can reach destination from src
                if src in has_path:
                    return True
                # no neighbors -> stuck at node "src"
                if len(neighbors[src]) == 0:
                    return False
                
                # go over all neighbors of src
                while neighbors[src]:
                    # remove any edge (src, dest)
                    dest = neighbors[src].pop()
                    if src == dest:
                        # no self-loops allowed between src and dest
                        return False
                    # do all paths from dest lead to destination?
                    dest_reached = dfs(dest)
                    if not dest_reached:
                        return False
                    # destination was reached
                    has_path.add(src)
                return True
            else:
                # we are at destination
                
                # no neighbors -> reached destination
                if len(neighbors[src]) == 0:
                    return True
                
                while neighbors[src]:
                    # remove edge (src, dest)
                    dest = neighbors[src].pop()
                    # no loops between source and destination
                    if src == dest or dest == source:
                        # no self-loops allowed betw src and dest
                        return False
                    dest_reached = dfs(dest)
                    if not dest_reached:
                        return False
                return True
        return dfs(source)