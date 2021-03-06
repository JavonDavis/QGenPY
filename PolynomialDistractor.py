from Polynomial import *


def poly_distractor_1(values):
    highest = highest_degree(values)
    return highest + 1


def poly_distractor_2(values):
    highest = highest_degree(values)
    return highest - 1000


def poly_distractor_3(values):
    highest = highest_degree(values)
    return highest + 100


def poly_distractor_4(values):
    highest = highest_degree(values)
    if highest < 0:
        return 0
    return highest / 2

