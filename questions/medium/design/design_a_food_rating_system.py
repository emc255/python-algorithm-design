"""
2353. Design a Food Rating System

Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system.
The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has
the highest rating for the given type of cuisine.
If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller
than string y if x comes before y in dictionary order,
that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i],
then x[i] comes before y[i] in alphabetic order.

Example 1:
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]

[

[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
["korean", "japanese", "japanese", "greek", "japanese", "korean"],
[9, 12, 8, 15, 14, 7]],

["korean"],
["japanese"],
["sushi", 16],
["japanese"],
["ramen", 16],
["japanese"]
]

Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

Constraints:
1 <= n <= 2 * 104
n == foods.length == cuisines.length == ratings.length
1 <= foods[i].length, cuisines[i].length <= 10
foods[i], cuisines[i] consist of lowercase English letters.
1 <= ratings[i] <= 108
All the strings in foods are distinct.
food will be the name of a food item in the system across all calls to changeRating.
cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
At most 2 * 104 calls in total will be made to changeRating and highestRated.


"""
from collections import defaultdict

from icecream import ic
from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Map food with its rating.
        self.food_rating_map = {}
        # Map food with cuisine it belongs to.
        self.food_cuisine_map = {}

        # Store all food of a cuisine in a set (to sort them on ratings/name)
        # Set element -> Tuple: (-1 * food_rating, food_name)
        self.cuisine_food_map = defaultdict(SortedSet)

        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # Insert the '(-1 * rating, name)' element in the current cuisine's set.
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))
        ic(self.food_rating_map)
        ic(self.food_cuisine_map)

    def change_rating(self, food: str, new_rating: int) -> None:
        # Fetch cuisine name for food.
        cuisine_name = self.food_cuisine_map[food]

        # Find and delete the element from the respective cuisine's set.
        old_element = (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine_name].remove(old_element)

        # Update food's rating in 'food_rating' map.
        self.food_rating_map[food] = new_rating
        # Insert the '(-1 * new rating, name)' element in the respective cuisine's set.
        self.cuisine_food_map[cuisine_name].add((-new_rating, food))

    def highest_rated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        # Return name of the highest-rated 'food' of 'cuisine'.
        return highest_rated[1]


foodie = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                     ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                     [9, 12, 8, 15, 14, 7])
foodie.change_rating("sushi", 22)
foodie.change_rating("ramen", 22)
ic(foodie.highest_rated("japanese"))
