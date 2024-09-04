"""
874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north.
The robot can receive a sequence of these three possible types of commands:
-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is
at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle,
then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from
the origin squared (i.e. if the distance is 5, return 25).

Note:
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].


Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation:
The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4),
which squared is 32 + 42 = 25 units away.

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation:
The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8),
which squared is 12 + 82 = 65 units away.

Example 3:
Input: commands = [6,-1,-1,6], obstacles = []
Output: 36
Explanation:
The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6),
which squared is 62 = 36 units away.

Constraints:
1 <= commands.length <= 104
commands[i] is either -2, -1, or an integer in the range [1, 9].
0 <= obstacles.length <= 104
-3 * 104 <= xi, yi <= 3 * 104
The answer is guaranteed to be less than 231.

"""
from icecream import ic


def robot_sim(commands: list[int], obstacles: list[list[int]]) -> int:
    result = 0
    x, y = 0, 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # north, east, south, west
    index_directions = 0
    obstacles_set = set(map(tuple, obstacles))  # convert obstacle list to a set of tuples

    for command in commands:
        if command == -1:
            # modded by the length of directions so index wont get out of bounce
            index_directions = (index_directions + 1) % 4
        elif command == -2:
            index_directions = (index_directions - 1) % 4
        else:
            dx, dy = directions[index_directions]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in obstacles_set:
                    break
                x, y = next_x, next_y
            result = max(result, x ** 2 + y ** 2)

    return result


ic(robot_sim([6, -1, -1, 6], []))
ic(robot_sim([4, -1, 4, -2, 4], [[2, 4]]))
