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

    # only one setup call
    mxb.setup()

    # have to keep tests in one block
    def tests(self):
        # test_a_hello_world
        qgen.test()

        # test_b_imports
        built_in_size = len(built_in)
        qgen.build_moodle_xml(TEST_IMPORTS_YML_PATH, question="SimplePolynomial", number_of_questions=2)
        self.assertGreater(len(qgen.functions), built_in_size, "No functions were imported")

        # test_b_generate_moodle_xml
        qgen.build_moodle_xml(TEST_SIMPLE_YML_PATH, question="SimpleAddition", number_of_questions=2)

        # test_a_sets
        qgen.build_moodle_xml(TEST_SETS_YML_PATH, question="SimpleSets", number_of_questions=2)

        # only one end tag call
        mxb.build_quiz_end_tag()


if __name__ == '__main__':
    unittest.main()
