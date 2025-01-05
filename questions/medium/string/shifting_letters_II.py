"""
2381. Shifting Letters II

You are given a string s of lowercase English letters and a 2D integer array
shifts where shifts[i] = [starti, endi, directioni]. For every i, shift
the characters in s from the index starti to the index endi (inclusive)
forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter
in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly,
shifting a character backward means replacing it with the previous letter
in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

Example 1:
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation:
Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

Example 2:
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation:
Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".

Constraints:
1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.

"""
from icecream import ic


def shifting_letters(s: str, shifts: list[list[int]]) -> str:
    result = list(s)  # Convert the string to a list for mutability
    for start, end, direction in shifts:
        for i in range(start, end + 1):
            d = 1 if direction == 1 else -1
            # Shift the character with modular arithmetic
            result[i] = chr((ord(result[i]) - ord('a') + d) % 26 + ord('a'))
    return "".join(result)


def shifting_letters_v2(s: str, shifts: list[list[int]]) -> str:
    cum_shifts = [0] * (len(s) + 1)

    for st, en, d in shifts:
        if d == 0:
            cum_shifts[st] -= 1
            cum_shifts[en + 1] += 1
        else:
            cum_shifts[st] += 1
            cum_shifts[en + 1] -= 1

    cum_sum = 0
    s = list(s)
    for i in range(len(s)):
        cum_sum += cum_shifts[i]

        new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
        s[i] = chr(new_code)

    return ''.join(s)


def shifting_letters_v3(s: str, shifts: list[list[int]]) -> str:
    n = len(s)
    net_shifts = [0] * (n + 1)  # One extra space for prefix sum calculation

    # Accumulate the shifts using prefix sum
    for start, end, direction in shifts:
        shift_value = 1 if direction == 1 else -1
        net_shifts[start] += shift_value
        net_shifts[end + 1] -= shift_value

    # Calculate the cumulative shifts
    for i in range(1, n):
        net_shifts[i] += net_shifts[i - 1]

    # Apply the shifts to the string
    result = [
        chr((ord(c) - ord('a') + net_shifts[i]) % 26 + ord('a'))
        for i, c in enumerate(s)
    ]

    return "".join(result)


ic(shifting_letters(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]))
ic(shifting_letters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]]))
