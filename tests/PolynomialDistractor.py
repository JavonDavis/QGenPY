def poly_distractor_1(polynomial):
    return str(polynomial.get_degree() + 1)


def poly_distractor_2(polynomial):
    return str(polynomial.get_degree() - 1000)


def poly_distractor_3(polynomial):
    return str(polynomial.get_degree() + 100)


def poly_distractor_4(polynomial):
    if polynomial.get_degree != 0:
        return "0"