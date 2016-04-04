import os
import sys
import unittest

import qgen
import qgen.generators.moodle_xml_builder as mxb
from qgen.built_in_functions import built_in_functions as built_in

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.getcwd())

TEST_0_YML_PATH = os.getcwd() + "/tests/test0.yml"
TEST_1_YML_PATH = os.getcwd() + "/tests/test1.yml"


class TestSuite(unittest.TestCase):
    """ test cases."""

    def test_a_hello_world(self):
        qgen.test()

    def test_b_imports(self):
        built_in_size = len(built_in)
        mxb.setup()
        qgen.build_moodle_xml(TEST_0_YML_PATH, question="SimplePolynomial", number_of_questions=2)
        mxb.build_quiz_end_tag()
        self.assertGreater(len(qgen.functions), built_in_size, "No functions were imported")

    def test_b_generate_moodle_xml(self):
        mxb.setup()
        qgen.build_moodle_xml(TEST_1_YML_PATH, question="SimpleAddition", number_of_questions=2)
        mxb.build_quiz_end_tag()


if __name__ == '__main__':
    unittest.main()
