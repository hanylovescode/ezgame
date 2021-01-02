import logging
from random import randint
import math


# TODO: try to make class Vector inherit from a Sequence (list, tuple, ...)
# TODO: check the difference between this and the Verlet method:
#   https://gamedev.stackexchange.com/a/41917


class Vector:
    """
    Implementation of a 2D Euclidean Vector and its methods.
    """
    logger = logging.getLogger('Vector')

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        self.logger.info(f'init -> Vector({x},{y})')

    @classmethod
    def from_tuple(cls, input_tuple: tuple[float, float]):
        """Initialize a Vector from a tuple"""
        return cls(input_tuple[0], input_tuple[1])

    @classmethod
    def create_from_random(cls, rand_min: int, rand_max: int):
        """Initialize a new Vector with a random x and y values"""
        return cls(randint(rand_min, rand_max), randint(rand_min, rand_max))

    def copy(self):
        """Returns a new instance with the current Vector values"""
        return Vector(self.x, self.y)

    def randomize_values(self, rand_bound: int, magnitude: float):
        """Changes the current Vector to random values"""
        self.x = randint(-rand_bound, rand_bound) * magnitude
        self.y = randint(-rand_bound, rand_bound) * magnitude

    def __eq__(self, other_vector):
        """Overriding == operator"""
        if not other_vector:
            return False
        return self.x == other_vector.x and self.y == other_vector.y

    def __repr__(self):
        """Overriding the __repr__ method; for debugging"""
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        """Overriding the __str__ method; for debugging"""
        return f'({self.x}, {self.y})'

    # Don't use this method, It's just for testing
    def __getitem__(self, i: int) -> float:
        """Overriding the __getitem__ method; for debugging"""
        self.logger.warning('You are using __getitem__, use .x or .y instead!')
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError

    # Don't use this method, It's just for testing
    def __add__(self, other_vector):
        """
        Overriding the addition operator.
        WARNING: It creates a new instance.
        """
        Vector.__confirm_is_vector(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        self.logger.warning('You created a new instance of the class Vector')
        return Vector(x, y)

    # Don't use this method, It's just for testing
    def __sub__(self, other_vector):
        """
        Overriding the subtraction operator.
        WARNING: It creates a new instance.
        """
        Vector.__confirm_is_vector(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        self.logger.warning('You created a new instance of the class Vector')
        return Vector(x, y)

    def add(self, other_vector):
        Vector.__confirm_is_vector(other_vector)
        self.x += other_vector.x
        self.y += other_vector.y

    def subtract(self, other_vector):
        Vector.__confirm_is_vector(other_vector)
        self.x -= other_vector.x
        self.y -= other_vector.y

    def multiply(self, magnitude: float):
        """scalar multiplication of the Vector"""
        self.x *= magnitude
        self.y *= magnitude

    def divide(self, magnitude: float):
        """scalar division of the Vector"""
        if magnitude == 0:
            raise ValueError('Dividing by zero!')
        self.multiply(1 / magnitude)

    def get_magnitude(self) -> float:
        """
        returns the magnitude of the Vector
        using the formula c^2 = a^2 + b^2
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        """changes the Vector to a unit Vector"""
        return self.divide(self.get_magnitude())

    def set_magnitude(self, magnitude: float):
        """change the magnitude of the vector to a specific value"""
        self.normalize()
        self.multiply(magnitude)

    def limit(self, bound: float):
        """Bounds the Vector values to specific limits"""
        # TODO: find if there's a better implementation
        if self.x > bound:
            self.x = bound
        elif self.x < -bound:
            self.x = -bound
        if self.y > bound:
            self.y = bound
        elif self.y < -bound:
            self.y = -bound

    def set(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def distance(vector_a, vector_b) -> float:
        """Returns the Euclidean distance between two Vectors"""
        Vector.__confirm_is_vector(vector_a)
        Vector.__confirm_is_vector(vector_b)
        # TODO: see if math.isclose() has better performance than math.dist()
        return math.dist((vector_a.x, vector_a.y), (vector_b.x, vector_b.y))

    @staticmethod
    def __confirm_is_vector(var):
        """Check if the variable is an instance of type Vector, and raise a TypeError if not"""
        if type(var) is not Vector:
            error_msg = f'{var} is an instance of class {type(var).__name__} and not of class Vector'
            raise TypeError(error_msg)
