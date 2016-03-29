from tests.context import qgen

import unittest


class TestSuite(unittest.TestCase):
    """ test cases."""

    def test_a_hello_world(self):
        qgen.test()

    def test_b_generate_moodle_xml(self):
        qgen.build_moodle_xml("/Users/javon/Desktop/Applications/Python/QGen/tests/test0.yml",question="SimpleAddition")

if __name__ == '__main__':
    unittest.main()