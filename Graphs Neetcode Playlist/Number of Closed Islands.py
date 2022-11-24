class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        
        def dfs(r,c):
            if grid[r][c]==1:
                return True
            if r<=0 or c<=0 or r==rows-1 or c==cols-1:
                return False
            grid[r][c]=1
            left=dfs(r,c-1)
            right=dfs(r,c+1)
            top=dfs(r-1,c)
            down=dfs(r+1,c)
            return left and right and top and down
        
        cnt=0
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if grid[i][j]==0 and dfs(i,j):
                    cnt+=1
        return cnt