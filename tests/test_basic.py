from tests.context import qgen

import unittest
import os

TEST_0_YML_PATH = os.getcwd() + "/tests/test0.yml"
TEST_1_YML_PATH = os.getcwd() + "/tests/test1.yml"


class TestSuite(unittest.TestCase):
    """ test cases."""

    def test_a_hello_world(self):
        qgen.test()

    def test_b_poly(self):
        qgen.test_polynomial()

    def test_b_generate_moodle_xml(self):
        qgen.build_moodle_xml(TEST_0_YML_PATH, question="SimplePolynomial", number_of_questions=10)

    def test_b_generate_moodle_xml_2(self):
        qgen.build_moodle_xml(TEST_1_YML_PATH, question="SimpleAddition", number_of_questions=10)


if __name__ == '__main__':
    unittest.main()
