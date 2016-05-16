import os
import sys
import unittest

import qgen
import qgen.generators.moodle_xml_builder as mxb
from qgen.built_in_functions import built_in_functions as built_in
from qgen.qgen_exceptions import InvalidConfigException

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.getcwd())

TEST_IMPORTS_YML_PATH = os.getcwd() + "/tests/test_imports.yml"
TEST_SIMPLE_YML_PATH = os.getcwd() + "/tests/test_simple.yml"
TEST_SETS_YML_PATH = os.getcwd() + "/tests/test_sets.yml"
TEST_BAD_YML_PATH = os.getcwd() + "/tests/test_missing_config.yml"
TEST_CODE_BLOCK_YML_PATH = os.getcwd() + "/tests/test_code_block.yml"
TEST_NO_REPEATS_PATH = os.getcwd() + "/tests/test_no_repetitions.yml"
TEST_NO_REPEATS_PATH_2 = os.getcwd() + "/tests/test_no_repetitions_2.yml"


class TestSuite(unittest.TestCase):
    """ test cases."""

    def test_b_imports(self):
        built_in_size = len(built_in)
        qgen.build_moodle_xml(TEST_IMPORTS_YML_PATH, question="SimplePolynomial", number_of_questions=5)
        self.assertGreater(len(qgen.functions), built_in_size, "No functions were imported")

    def test_b_generate_moodle_xml(self):
        qgen.build_moodle_xml(TEST_SIMPLE_YML_PATH, question="SimpleAddition", number_of_questions=2)

    def test_a_sets(self):
        qgen.build_moodle_xml(TEST_SETS_YML_PATH, question="SimpleSets", number_of_questions=7)

    def test_missing_config(self):
        with self.assertRaises(InvalidConfigException):
            qgen.build_moodle_xml(TEST_BAD_YML_PATH, question="SimpleAddition", number_of_questions=2)

    def test_foo_1(self):
        qgen.build_moodle_xml(TEST_CODE_BLOCK_YML_PATH, question="SimpleFoo1", number_of_questions=10)

    def test_no_repetitions(self):
        """Should only generate one question vs the 2 requested"""
        qgen.build_moodle_xml(TEST_NO_REPEATS_PATH, question="SimpleRepetition", number_of_questions=2)

    def test_no_repetitions_b(self):
        """Should only generate one question vs the 2 requested and with only one answer vs the two that are the same"""
        qgen.build_moodle_xml(TEST_NO_REPEATS_PATH_2, question="SimpleRepetition", number_of_questions=1)

if __name__ == '__main__':
    unittest.main()
