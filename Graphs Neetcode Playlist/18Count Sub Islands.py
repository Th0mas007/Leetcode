class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        rows,cols=len(grid1),len(grid1[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or grid2[r][c]==0:
                return True
            # If one of the cells in either grid is land and the other is water, then the current cell can **not** be a sub-island.
            elif (grid1[r][c]==1 and grid2[r][c]==0) or (grid1[r][c]==0 and grid2[r][c]==1):
                return False
            # If the cell in both grids is land, we want to change the value so we don't check this same cell later.
            elif grid1[r][c]==1 and grid2[r][c]==1:
                grid2[r][c]=0
                left=dfs(r+1,c)
                right=dfs(r-1,c)
                top=dfs(r,c-1)
                bot=dfs(r,c+1)
            # If all directions of a land cell in grid2 match with corresponding land cells in grid1, then a sub-island was found.
                return left and right and top and bot
            
        res=0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]==1 and dfs(i,j):
                    res+=1
        return res
                    
            
            
        