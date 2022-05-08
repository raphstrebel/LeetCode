class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Time: O(E + V^2 * log(V)) since:
            - lexical sorting requires O(V^2 * log(V)) in the worst case (complete graph) since we sort V vertices for all vertices
            - DFS requires O(E) operations (we go over each edge once)
            
        Space: O(E + V) since we store the graph as an adjacency list
        """
        if len(tickets) == 0:
            return []

        # build adjacency list of nodes to neighbors
        neighbors = defaultdict(list)
        for src, dest in tickets:
            # might be multiple same (src, dest) tickets
            neighbors[src].append(dest)
        # sort destinations by lexical order
        for src, dest_list in neighbors.items():
            dest_list.sort(reverse=True)
        
        max_path = []
        def dfs(src):
            # while there are still neighbors to this source
            while neighbors[src]:
                # iterate over all neighbors recursively
                dest = neighbors[src].pop()
                dfs(dest)
            # there are no more neighbors to src, so add src to max_path
            max_path.append(src)
        dfs('JFK')
        # reverse max_path since source gets added after all destinations
        return max_path[::-1]
