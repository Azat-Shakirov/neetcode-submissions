class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, s in enumerate(row):
                if s == ".":
                    continue
                box = (i // 3) * 3 + (j // 3)

                if s in rows[i] or s in cols[j] or s in boxes[box]:
                    return False
                rows[i].add(s)
                cols[j].add(s)
                boxes[box].add(s)
        return True