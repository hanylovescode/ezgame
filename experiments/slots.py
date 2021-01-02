from timeit import timeit
from random import randint

INSTANCES_COUNT = 10 ** 6
REPETITIONS = 10
RAND_MIN = -1000
RAND_MAX = 1000


class VectorNormal:
    def __init__(self):
        self.x = randint(RAND_MIN, RAND_MAX)
        self.y = randint(RAND_MIN, RAND_MAX)


class VectorSlots:
    __slots__ = ['x', 'y']

    def __init__(self):
        self.x = randint(RAND_MIN, RAND_MAX)
        self.y = randint(RAND_MIN, RAND_MAX)


def create_normal_vectors():
    vectors = []
    for i in range(INSTANCES_COUNT):
        vectors.append(VectorNormal())
    # print(vectors.__sizeof__())


def create_slots_vectors():
    vectors = []
    for i in range(INSTANCES_COUNT):
        vectors.append(VectorSlots())
    # print(vectors.__sizeof__())


if __name__ == '__main__':
    normal_time = timeit(create_normal_vectors, number=REPETITIONS)
    print('normal time:', normal_time)

    slots_time = timeit(create_slots_vectors, number=REPETITIONS)
    print('slots time:', slots_time)

    normal_time = timeit(create_normal_vectors, number=REPETITIONS)
    print('normal time:', normal_time)
