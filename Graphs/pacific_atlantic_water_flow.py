class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if len(matrix) == 0:
            return None
        
        check_pacific = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        check_atlantic = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        list_to_return = []
        
        
        def dfs(matrix,row,col,prevVal,ocean):
            if row < 0 or col < 0 or row > num_rows -1 or col > num_cols -1:
                return  # index is out of bounds
            elif prevVal > matrix[row][col]:
                return  # does not meet the conditions for water floe
            elif ocean[row][col] == 1:
                return # we have already processed this cell
            
            ocean[row][col] = 1     # mark this cell as processed (water passes through)
            
            # Call DFS on neighboring cells
            
            dfs(matrix,row - 1,col,matrix[row][col],ocean)
            dfs(matrix,row + 1,col,matrix[row][col],ocean)
            dfs(matrix,row,col - 1,matrix[row][col],ocean)
            dfs(matrix,row,col + 1,matrix[row][col],ocean)
            
            return
            
            
        for i in range(num_cols):
            dfs(matrix,0,i,-1,check_pacific)
        for i in range(num_cols):
            dfs(matrix,num_rows-1,i,-1,check_atlantic)
        for i in range(num_rows):
            dfs(matrix,i,0,-1,check_pacific)
        for i in range(num_rows):
            dfs(matrix,i,num_cols -1, -1, check_atlantic)
            
        for i in range(num_rows):
            for j in range(num_cols):
                if check_pacific[i][j] == 1 and check_atlantic[i][j] == 1:
                    list_to_return.append(list([i,j]))
            
        print(check_pacific)
        print(check_atlantic)
        
        return list_to_return