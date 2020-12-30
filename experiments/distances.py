import timeit
import numpy as np
import math


def numpy_distance_a():
    point1 = np.array((1, 2))
    point2 = np.array((20, 30))

    distance = np.linalg.norm(point1 - point2)

    # print(distance)


def numpy_distance_b():
    point1 = np.array((1, 2))
    point2 = np.array((20, 30))

    distance = np.sqrt(np.sum((point2 - point1) ** 2))

    # print(distance)


def python_distance_a():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = math.sqrt(
        math.pow(point2[0] - point1[0], 2) +
        math.pow(point2[1] - point1[1], 2)
    )

    # print(distance)


def python_distance_b():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )

    # print(distance)


def python_distance_c():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = math.sqrt(
        ((point2[0] - point1[0]) * (point2[0] - point1[0])) +
        ((point2[1] - point1[1]) * (point2[1] - point1[1]))
    )

    # print(distance)


def python_distance_d():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = math.pow(
        ((point2[0] - point1[0]) * (point2[0] - point1[0])) +
        ((point2[1] - point1[1]) * (point2[1] - point1[1])), 0.5
    )

    # print(distance)


def python_distance_e():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = (((point2[0] - point1[0]) * (point2[0] - point1[0])) +
                ((point2[1] - point1[1]) * (point2[1] - point1[1]))
                ) ** 0.5

    # print(distance)


def python_distance_f():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = (math.pow(point2[0] - point1[0], 2) +
                math.pow(point2[1] - point1[1], 2)
                ) ** 0.5

    # print(distance)


def python_distance_g():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = math.pow(math.pow(point2[0] - point1[0], 2) +
                        math.pow(point2[1] - point1[1], 2)
                        , 0.5)

    # print(distance)


def python_distance_h():
    point1 = (1, 2)
    point2 = (20, 30)

    distance = math.dist(point2, point1)

    # print(distance)


if __name__ == '__main__':
    n = 10000

    numpy_time_a = timeit.timeit(numpy_distance_a, number=n)
    print(f'numpy  distance_a (linalg.norm) : {round(numpy_time_a, 5)}')

    numpy_time_b = timeit.timeit(numpy_distance_b, number=n)
    print(f'numpy  distance_b (sqrt,sum,**2): {round(numpy_time_b, 5)}')

    python_time_a = timeit.timeit(python_distance_a, number=n)
    print(f'python distance_a (sqrt,pow)    : {round(python_time_a, 5)}')

    python_time_b = timeit.timeit(python_distance_b, number=n)
    print(f'python distance_b (sqrt,**)     : {round(python_time_b, 5)}')

    python_time_c = timeit.timeit(python_distance_c, number=n)
    print(f'python distance_c (sqrt,*)      : {round(python_time_c, 5)}')

    python_time_d = timeit.timeit(python_distance_d, number=n)
    print(f'python distance_d (pow0.5,*)    : {round(python_time_d, 5)}')

    python_time_e = timeit.timeit(python_distance_e, number=n)
    print(f'python distance_e (**0.5,*)     : {round(python_time_e, 5)}')

    python_time_f = timeit.timeit(python_distance_f, number=n)
    print(f'python distance_f (**0.5,pow)   : {round(python_time_f, 5)}')

    python_time_g = timeit.timeit(python_distance_g, number=n)
    print(f'python distance_g (pow0.5,pow)  : {round(python_time_g, 5)}')

    python_time_h = timeit.timeit(python_distance_h, number=n)
    print(f'python distance_h (dist)        : {round(python_time_h, 5)}')