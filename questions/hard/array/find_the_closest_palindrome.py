"""
564. Find the Closest Palindrome

Given a string n representing an integer,
return the closest integer (not including itself),
which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized
between two integers.



Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"
Explanation:
0 and 2 are the closest palindromes but we return the smallest which is 0.

Constraints:
1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].

"""
from icecream import ic


def nearest_palindromic(n: str) -> str:
    if len(n) == 1 or int(n) == 10:
        return "0" if int(n) <= 0 else int(n) - 1

    l, r = 0, len(n) - 1
    result = []
    while l < r:
        if n[l] == n[r]:
            continue
        else:
            left = int(n[l])
            right = int(n[r])
            while left != right:
                if right > left:
                    right -= 1
                elif right < left:
                    right += 1
            result.append(str(left))

        l += 1
        r -= 1
    m = ""
    if l == r:
        m = n[l]

    return "".join(result) + m + "".join(result[::-1])


def nearest_palindromic_v2(n):
    if n == "1":
        return "0"

    length = len(n)
    candidates = set()

    # Add 999...999 and 1000...0001 for edge cases like 1000, 10000
    candidates.add(str(10 ** (length - 1) - 1))  # like 999 for 1000
    candidates.add(str(10 ** length + 1))  # like 1001 for 1000

    # Generate the palindrome by mirroring the first half
    prefix = n[:(length + 1) // 2]
    for i in [-1, 0, 1]:
        new_prefix = str(int(prefix) + i)
        if length % 2 == 0:
            candidate = new_prefix + new_prefix[::-1]
        else:
            candidate = new_prefix + new_prefix[:-1][::-1]
        candidates.add(candidate)

    candidates.discard(n)  # Remove the original number if it's a palindrome

    # Find the closest palindrome
    closest = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
    return closest


# Example usage
ic(nearest_palindromic_v2("123"))  # Output should be "121"
ic(nearest_palindromic_v2("10"))

ic(nearest_palindromic("1"))
ic(nearest_palindromic("10"))
ic(nearest_palindromic("1263"))
ic(nearest_palindromic("125"))
