"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""


def common_longest_prefix(strs: list) -> str:
    def common_prefix(s1: str, s2: str) -> str:
        index = 0
        prefix = ""
        while index < len(s1) and index < len(s2):
            if s1[index] != s2[index]:
                return prefix
            prefix += s1[index]
            index += 1
        return prefix

    if len(strs) <= 1:
        return strs[0]

    longest_prefix = common_prefix(strs[0], strs[1])

    for i in range(2, len(strs)):
        last_index = len(longest_prefix)

        if last_index == 0:
            return ""

        prefix_to_compare = strs[i][:last_index]
        while prefix_to_compare != longest_prefix:
            last_index -= 1
            longest_prefix = longest_prefix[:last_index]
            prefix_to_compare = prefix_to_compare[:last_index]

    return longest_prefix


print(common_longest_prefix(["flower", "flow", "flight"]))
print(common_longest_prefix(["dog", "racecar", "car"]))
print(common_longest_prefix([""]))
