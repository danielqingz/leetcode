# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

class DetectSquares:

    def __init__(self):
        self.map = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.map[y][x] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        if not y in self.map:
            return 0
        yCnt = self.map[y]

        for col, colCnt in self.map.items():
            if col != y:
                # 根据对称性，这里可以不用取绝对值
                d = col - y
                res += colCnt[x] * yCnt[x + d] * colCnt[x + d]
                res += colCnt[x] * yCnt[x - d] * colCnt[x - d]
        
        return res