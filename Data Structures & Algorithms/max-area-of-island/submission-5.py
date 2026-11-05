class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        #make this a dict of lists of coords
        gridSet = set()
        mappedAreas = []
        currLi = []

        def helper(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in gridSet or grid[x][y] == 0:
                return
            
            gridSet.add((x, y))
            currLi.append((x, y))

            helper(x - 1, y)
            helper(x + 1, y)
            helper(x, y - 1)
            helper(x, y + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] not in gridSet:
                    currLi = []
                    helper(row, col)
                    if not currLi:
                        continue
                    mappedAreas += [currLi]

        if not mappedAreas:
            return 0
            
        return len(max(mappedAreas, key = len))