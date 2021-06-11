#1. BFS 
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        count = 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] == '0'
                    q = Queue(maxsize = 0)
                    q.put(r * nc + c)
                    while not q.empty():
                        idx = q.get()
                        row = idx // nc
                        col = idx % nc
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            q.put((row - 1) * nc + col)
                            grid[row - 1][col] = '0'
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            q.put((row + 1) * nc + col)
                            grid[row + 1][col] = '0'                            
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            q.put(row * nc + col - 1)
                            grid[row][col - 1] = '0'
                        if col + 1 < nc and grid[row][col + 1] == '1':
                            q.put(row * nc + col + 1)
                            grid[row][col + 1] = '0' 
        return count
      
      
#2. dfs

#3. union find
