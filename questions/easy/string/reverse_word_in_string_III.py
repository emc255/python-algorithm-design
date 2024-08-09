"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"


Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

"""
from icecream import ic


def reverse_words(s: str) -> str:
    words = s.split(" ")
    for i, word in enumerate(words):
        words[i] = word[::-1]

    return " ".join(words)


def reverse_words_v2(s: str) -> str:
    return " ".join(word[::-1] for word in s.split())


ic(reverse_words("Let's take LeetCode contest"))
ic(reverse_words_v2("Let's take LeetCode contest"))
