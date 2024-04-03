"""
Word Search

Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?

"""
from icecream import ic


def exist(board: list[list[str]], word: str) -> bool:
    def backtrack(r, c, i):
        # Base Case
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
            return False

        # Word found
        if i == len(word) - 1:
            return True

        # Mark current cell as visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore in all directions
        for dr, dc in directions:
            if backtrack(r + dr, c + dc, i + 1):
                return True

        # Restore the cell
        board[r][c] = temp
        return False

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Up, Down, Right, Left
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True

    return False


ic(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
