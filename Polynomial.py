import random


class Polynomial():
    st = range(0, 149)

    def __init__(self):
        self.degree = 0
        self.generate()

    def generate(self):
        self.degree = random.choice(Polynomial.st)
        Polynomial.st.pop()

    def __str__(self):
        return "x^" + str(self.degree)

    def get_degree(self):
        return self.degree


def poly_random(values):
    polynomials = []
    for i in range(0, values['count']):
        poly1 = Polynomial()
        poly2 = Polynomial()
        poly3 = Polynomial()
        polynomial = str(poly1) + " + " + str(poly2) + " + " + str(poly3)
        polynomials.append(polynomial)
    return polynomials


def highest_degree(poly):
    polys = poly.split("+")
    polys = map(lambda x: x.replace("x^", ""), polys)
    degrees = map(int, polys)
    return max(degrees)
