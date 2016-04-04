from Polynomial import *


def poly_distractor_1(polynomial):
    highest = highest_degree(polynomial)
    return highest + 1


def poly_distractor_2(polynomial):
    highest = highest_degree(polynomial)
    return highest - 1000


def poly_distractor_3(polynomial):
    highest = highest_degree(polynomial)
    return highest + 100


def poly_distractor_4(polynomial):
    highest = highest_degree(polynomial)
    if highest < 0:
        return 0
    return highest /2
