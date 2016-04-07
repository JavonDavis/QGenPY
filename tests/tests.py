import os
import sys
import unittest

import qgen
import qgen.generators.moodle_xml_builder as mxb
from qgen.built_in_functions import built_in_functions as built_in

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.getcwd())

TEST_IMPORTS_YML_PATH = os.getcwd() + "/tests/test_imports.yml"
TEST_SIMPLE_YML_PATH = os.getcwd() + "/tests/test_simple.yml"
TEST_SETS_YML_PATH = os.getcwd() + "/tests/test_sets.yml"


class TestSuite(unittest.TestCase):
    """ test cases."""

    def test_a_hello_world(self):
        qgen.test()

    def test_b_imports(self):
        built_in_size = len(built_in)
        qgen.build_moodle_xml(TEST_IMPORTS_YML_PATH, question="SimplePolynomial", number_of_questions=5)
        self.assertGreater(len(qgen.functions), built_in_size, "No functions were imported")

    def test_b_generate_moodle_xml(self):
        qgen.build_moodle_xml(TEST_SIMPLE_YML_PATH, question="SimpleAddition", number_of_questions=2)

    def test_a_sets(self):
        qgen.build_moodle_xml(TEST_SETS_YML_PATH, question="SimpleSets", number_of_questions=2)

if __name__ == '__main__':
    unittest.main()
