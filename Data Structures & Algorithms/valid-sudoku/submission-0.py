class Solution:
    def checkBiome(self, biome):
        s = set()

        for x in biome:
            if x == ".":
                continue
            if x not in list("123456789"):
                return False
            if x in s:
                return False
            
            s.add(x)

        return True

    def isValidBiomes(self, biomes):
        for biome in biomes:
            if not self.checkBiome(biome):
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        rows = [row for row in board]
        cols = [[row[i] for row in board] for i in range(9)]
        sub_boxes = []
        for i in range(3):
            for j in range(3):
                base_col = 3*i
                base_row = 3*j

                sub_box = [board[base_row][base_col], board[base_row][base_col+1], board[base_row][base_col+2],
                           board[base_row+1][base_col], board[base_row+1][base_col+1], board[base_row+1][base_col+2],
                           board[base_row+2][base_col], board[base_row+2][base_col+1], board[base_row+2][base_col+2]]
                
                sub_boxes.append(sub_box)
        
        return (self.isValidBiomes(rows) and self.isValidBiomes(cols) and self.isValidBiomes(sub_boxes))