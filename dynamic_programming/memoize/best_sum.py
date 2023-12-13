from typing import Union


def best_sum(target_sum: int, numbers: list, memoize: dict = None) -> Union[list, None]:
    if memoize is None:
        memoize = {}

    if target_sum in memoize:
        return memoize[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination = []
    for number in numbers:
        remainder = target_sum - number
        """
        The problem is related to the recursive call and the modification of the combination list. 
        Since combination is a list, when you pass it to the recursive call 
        and then modify it with combination.append(number), 
        it affects all the previous calls in the recursion stack.
        
        To fix this, you need to create a copy of the combination list before passing it to 
        the recursive call. 
        You can use the list() constructor to make a shallow copy. 
        Additionally, the base cases for the function should be placed before the recursive call.
        """
        combination = best_sum(remainder, numbers, memoize)

        if combination is not None:
            current_combination = list(combination)
            current_combination.append(number)
            if len(shortest_combination) == 0 or len(current_combination) < len(shortest_combination):
                shortest_combination = list(current_combination)

    memoize[target_sum] = shortest_combination

    return shortest_combination


print(best_sum(8, [2, 3, 5]))
print(best_sum(100, [1, 2, 3, 25]))
