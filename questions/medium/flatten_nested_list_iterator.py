"""
341. Flatten Nested List Iterator

You are given a nested list of integers nestedList.
Each element is either an integer or a list whose elements may also be integers or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].

Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].

"""


class NestedInteger:
    def __init__(self, nested_integer):
        if isinstance(nested_integer, list):
            self.nested_integer = []
            for i in nested_integer:
                self.nested_integer.append(NestedInteger(i))
        elif isinstance(nested_integer, int):
            self.nested_integer = nested_integer

    def is_integer(self) -> bool:
        """
           @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.nested_integer, int)

    def get_integer(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if isinstance(self.nested_integer, int):
            return self.nested_integer

    def get_list(self) -> ['NestedInteger']:
        """
           @return the nested list that this NestedInteger holds, if it holds a nested list
           Return None if this NestedInteger holds a single integer
        """
        if isinstance(self.nested_integer, list):
            return self.nested_integer


class NestedIterator:
    # def __init__(self, nested_list: ['NestedInteger']):
    #     def flatten(nested_integer):
    #         for number in nested_integer:
    #             if number.isInteger():
    #                 self.flatten_list.append(number.getInteger())
    #             else:
    #                 flatten(number.getList())
    #
    #     self.flatten_list = []
    #     self.current_index = 0
    #     flatten(nested_list)

    def __init__(self, nested_list: ['NestedInteger']):
        def flatten(nested_integer):
            if nested_integer is None:
                return
            
            if nested_integer.isInteger():
                self.flatten_list.append(nested_integer.getInteger())

            else:
                for sublist in nested_integer.getList():
                    flatten(sublist)

        self.flatten_list = []
        self.current_index = 0
        for ni in nested_list:
            flatten(ni)

    def next(self) -> int:
        value = self.flatten_list[self.current_index]
        self.current_index += 1
        return value

    def has_next(self) -> bool:
        return self.current_index < len(self.flatten_list)
