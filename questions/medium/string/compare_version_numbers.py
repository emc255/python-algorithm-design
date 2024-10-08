"""
165. Compare Version Numbers

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'.
Each revision consists of digits and may contain leading zeros.
Every revision contains at least one character.
Revisions are 0-indexed from left to right,
with the leftmost revision being revision 0,
the next revision being revision 1, and so on.
For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order.
Revisions are compared using their integer value ignoring any leading zeros.
This means that revisions 1 and 001 are considered equal.
If a version number does not specify a revision at an index,
then treat the revision as 0. For example,
version 1.0 is less than version 1.1 because their revision 0s are the same,
but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Example 1:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes,
both "01" and "001" represent the same integer "1".

Example 2:
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2,
which means it is treated as "0".

Example 3:
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0",
while version2's revision 0 is "1". 0 < 1, so version1 < version2.

Constraints:
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.

"""
from icecream import ic


def compare_version(version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")
    n1 = []
    n2 = []
    for i in range(len(v1)):
        if i == 0:
            if v1[i] == "" or v1[i] == "0":
                n1.append(0)
            else:
                try:
                    n1.append(int(v1[i]))
                except ValueError:
                    n1.append(0)
        elif v1[i].isdigit():
            n1.append(int(v1[i]))

    for i in range(len(v2)):
        if i == 0:
            if v2[i] == "" or v2[i] == "0":
                n2.append(0)
            else:
                try:
                    n2.append(int(v2[i]))
                except ValueError:
                    n2.append(0)
        elif v2[i].isdigit():
            n2.append(int(v2[i]))

    for i in range(max(len(n1), len(n2))):
        num1 = n1[i] if i < len(n1) else 0
        num2 = n2[i] if i < len(n2) else 0
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
    return 0


def compare_version_v2(version1: str, version2: str) -> int:
    version1 = version1.split('.')
    version2 = version2.split('.')
    ml = min(len(version1), len(version2))
    for i in range(ml):
        v1 = int(version1[i])
        v2 = int(version2[i])
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
    version = version1 if len(version1) - ml > 0 else version2
    v = 1 if len(version1) - ml > 0 else 2
    for i in range(ml, len(version)):
        if int(version[i]) > 0:
            return 1 if v == 1 else -1
    return 0


ic(compare_version("1.01", "1.001"))
ic(compare_version("0.1", "1.0"))
