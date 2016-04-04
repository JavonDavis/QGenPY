import moodle_xml_builder as mxb
from qgen.build_helpers import *

"""Functions to generate questions in different formats"""


def gen_moodle_xml(question):
    """Function to generate the questions in Moodle XML format"""
    params = {}
    for key, value in question.question_params.iteritems():
        try:
            params[key] = value.pop()
        except IndexError as e:
            print e
    print question.body.format(**params)
    print "********Options*********"

    body_for_xml = question.body.format(**params)
    mxb.build_question_for_xml(question.title, body_for_xml, question.type)

    # Evaluate answers
    for answer in question.answers:
        answer = evaluate_functions(answer, params)
        answer = evaluate_blocks(answer, params)
        mxb.build_answer_for_xml(answer)
        print answer

    # Evaluate distractors
    for distractor in question.distractors:
        distractor = evaluate_functions(distractor, params)
        distractor = evaluate_blocks(distractor, params)
        mxb.build_answer_for_xml(distractor)
        print distractor
    mxb.build_question_end_tag()
