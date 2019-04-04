class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        leftRight = []
        for row in grid:
            leftRight.append(max(row))
        topBottom = []
        for column in zip(*grid):
            topBottom.append(max(column))
        
        diffMatrix = []
        for rowIndex, row in enumerate(grid):
            diffMatrix.append([min(leftRight[rowIndex], topBottom[columnIndex]) - x for columnIndex, x in enumerate(row)])
        
        return sum(map(sum, diffMatrix))