"""
726. Number of Atoms

Given a string formula representing a chemical formula,
return the count of each atom.

The atomic element always starts with an uppercase character,
then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow
if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in
the following form: the first name (in sorted order), followed by its count
(if that count is more than 1), followed by the second name (in sorted order),
followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example 1:
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Constraints:
1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

"""
import collections

from icecream import ic


def count_of_atoms(formula: str) -> str:
    def multiply_counts(counts, multiplier):
        for k in counts:
            counts[k] *= multiplier
        return counts

    stack = []
    current_counts = collections.defaultdict(int)
    i, n = 0, len(formula)

    while i < n:
        if formula[i] == '(':
            stack.append(current_counts)
            current_counts = collections.defaultdict(int)
            i += 1
        elif formula[i] == ')':
            i += 1
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            multiplier = int(formula[start:i] or 1)
            current_counts = multiply_counts(current_counts, multiplier)
            if stack:
                previous_counts = stack.pop()
                for key, value in current_counts.items():
                    previous_counts[key] += value
                current_counts = previous_counts
        else:
            start = i
            i += 1
            while i < n and formula[i].islower():
                i += 1
            element = formula[start:i]
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            count = int(formula[start:i] or 1)
            current_counts[element] += count

    result = []
    for element in sorted(current_counts.keys()):
        result.append(element)
        if current_counts[element] > 1:
            result.append(str(current_counts[element]))

    return ''.join(result)


def count_of_atoms_v2(formula: str) -> str:
    def parse_formula(formula):
        stack = [collections.defaultdict(int)]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                top = stack.pop()
                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * multiplier
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][elem] += count

        return stack[0]

    element_counts = parse_formula(formula)
    sorted_elements = sorted(element_counts.items())
    result = []

    for elem, count in sorted_elements:
        result.append(elem)
        if count > 1:
            result.append(str(count))

    return ''.join(result)


def main():
    formula = "K4(ON(SO3)2)2"
    ic(count_of_atoms(formula))


main()
