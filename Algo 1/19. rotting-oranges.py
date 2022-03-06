class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """BFS solution"""
        n = len(grid)
        m = len(grid[0])
        
        # queue contains indices of rotten oranges
        queue = []
        num_fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue.append((-1,-1))
        time = 0
        while len(queue) != 0:
            i, j = queue.pop(0)
            if i == -1:
                time += 1
                if len(queue) == 0:
                    if num_fresh != 0:
                        # some fresh oranges are never rotten
                        return -1
                    return time -1 
                queue.append((-1,-1))
            else:
                # spread to neighbours of rotten orange
                for dir_ in dirs:
                    next_i = i + dir_[0]
                    next_j = j + dir_[1]
                    if 0 <= next_i < n and 0 <= next_j < m:
                        if grid[next_i][next_j] == 1:
                            # spread to this fresh orange
                            num_fresh -= 1
                            grid[next_i][next_j] = 2
                            queue.append((next_i, next_j))
        if num_fresh != 0:
            # some fresh oranges are never rotten
            return -1
        return time -1 