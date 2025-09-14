"""
966. Vowel Spellchecker

Given a wordlist, we want to implement a spellchecker that converts
a query word into a correct word.

For a given query word, the spell checker handles two categories
of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive),
then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the
query word with any vowel individually, it matches a word in the wordlist (case-insensitive),
then the query word is returned with the same case as the match in the wordlist.

Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].



Example 1:

Input:
wordlist = ["KiTe","kite","hare","Hare"],
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

Example 2:
Input:
wordlist = ["yellow"],
queries = ["YellOw"]
Output: ["yellow"]

Constraints:
1 <= wordlist.length, queries.length <= 5000
1 <= wordlist[i].length, queries[i].length <= 7
wordlist[i] and queries[i] consist only of only English letters.

"""
from icecream import ic


def spell_checker(word_list: list[str], queries: list[str]) -> list[str]:
    def vowel_wildcard(s: str) -> str:
        """Replace vowels with '*' for vowel-error matching."""
        return "".join('*' if ch in vowels else ch for ch in s.lower())

    vowels = set("aeiou")
    # 1. Exact matches
    exact_words = set(word_list)

    # 2. Case-insensitive matches
    case_insensitive = {}
    for word in word_list:
        lower_word = word.lower()
        if lower_word not in case_insensitive:  # first occurrence wins
            case_insensitive[lower_word] = word

    # 3. Vowel-error matches
    vowel_map = {}
    for word in word_list:
        word_wildcard = vowel_wildcard(word)
        if word_wildcard not in vowel_map:  # first occurrence wins
            vowel_map[word_wildcard] = word

    # Answer queries
    result = []
    for q in queries:
        if q in exact_words:  # Rule 1
            result.append(q)
        elif q.lower() in case_insensitive:  # Rule 2
            result.append(case_insensitive[q.lower()])
        elif vowel_wildcard(q) in vowel_map:  # Rule 3
            result.append(vowel_map[vowel_wildcard(q)])
        else:  # Rule 4
            result.append("")

    return result


ic(spell_checker(word_list=["KiTe", "kite", "hare", "Hare"],
                 queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
