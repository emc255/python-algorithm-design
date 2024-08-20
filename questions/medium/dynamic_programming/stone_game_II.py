"""
1140. Stone Game II

Alice and Bob continue their games with piles of stones.
There are a number of piles arranged in a row,
and each pile has a positive integer number of stones piles[i].
The obiective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first. Initially, m = 1.

On each player's turn, that player can take all
the stones in the first X remaining piles, where 1 <= X <= 2m.
Then, we set m = max(m, X).

The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally,
return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:
If Alice takes one pile at the beginning, Bob takes two piles,
then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total.
If Alice takes two piles at the beginning, then Bob can take all three piles left.
In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 104

"""
from icecream import ic


def stone_game_ii(piles: list[int]) -> int:
    def dfs(is_alice_turn, index, m):
        if index == len(piles):
            return 0

        if (is_alice_turn, index, m) in memo:
            return memo[(is_alice_turn, index, m)]

        result = 0 if is_alice_turn else float('inf')
        total = 0
        for i in range(1, 2 * m + 1):
            if index + i > len(piles):
                break
            total += piles[index + i - 1]
            if is_alice_turn:
                result = max(result, total + dfs(not is_alice_turn, index + i, max(m, i)))
            else:
                result = min(result, dfs(not is_alice_turn, index + i, max(m, i)))

        memo[(is_alice_turn, index, m)] = result
        return result

    memo = {}
    return dfs(True, 0, 1)


ic(stone_game_ii([2, 7, 9, 4, 4]))
