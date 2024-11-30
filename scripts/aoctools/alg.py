import operator as op
import collections
import itertools
import functools
import dataclasses
import math
import typing

"""
@dataclasses.dataclass
class point:
    x: int
    y: int

    def __len__(self):
        return abs(x) + abs(y)
    
    def __str__(self):
        return f"({x}, {y})"

    def __iter__(self):
        return iter((self.x, self.y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: "point") -> "point":
        return point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "point") -> "point":
        return point(self.x - other.x, self.y - other.y)
    
    @functools.cached_property 
    def angle(self) -> float:
        return atan2(self.y, self.x)

    @property
    def mag2(self) -> int:
        return self.x ** 2 + self.y ** 2

    @functools.cached_property 
    def mag(self) -> float:
        return math.sqrt(self.mag2())

    @functools.cached
    def as_ratio(self) -> typing.Tuple[int, int]:
        d = math.gcd(self.x, self.y)
        return self.x // d, self.y // d

    def dot(self, other: "point") -> int:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: "point") -> float:
        return math.acos(self.dot(other) / self.mag / other.mag)

    def angle_order(self, other: "point") -> float:
        return other.angle - self.angle if self.angle < other.angle
               else (2*math.pi + other.angle) - self.angle
        
@dataclass
class line:
    start: point
    end: point

    def __hash__(self):
        return hash((self.start, self.end))

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_horizontal(self):
        return self.start.y == self.end.y

    def __len__(self):
        return len(self.end - self.start)
"""

def rle(a, f = None, key = None):
    le = []
    p = None
    f = op.eq if f is None else f
    for x in a:
        if p is None:
            p = x, 1
        elif (key is None and f(p[0], x)) or (key is not None and f(key(p[0]), key(x))):
            p = x, p[1] + 1
        else:
            yield p
            p = x, 1
    yield p

# from itertools recipy
def win(a, n = 2):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(a)
    window = collections.deque(itertools.islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)
