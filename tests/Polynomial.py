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
        polynomial = Polynomial()
        polynomials.append(polynomial)
    return polynomials

def highest_degree(polynomials):
    # degrees = [polynomial.get_degree() for polynomial in polynomials]
    # return max(degrees)
    return polynomials.get_degree()