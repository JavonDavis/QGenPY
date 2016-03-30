from tests.context import qgen

import unittest


class TestSuite(unittest.TestCase):
    """ test cases."""

    def test_a_hello_world(self):
        qgen.test()

    def test_b_poly(self):
        qgen.test_polynomial()

    def test_b_generate_moodle_xml(self):
        qgen.build_moodle_xml("/Users/javon/Desktop/Applications/Python/QGen/tests/test0.yml",question="SimplePolynomial", number_of_questions=10)

    def test_b_generate_moodle_xml_2(self):
        qgen.build_moodle_xml("/Users/javon/Desktop/Applications/Python/QGen/tests/test1.yml",
                              question="SimpleAddition", number_of_questions=10)


if __name__ == '__main__':
    unittest.main()