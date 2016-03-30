import yaml
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


def distractor_1(polynomial):
    return str(polynomial.get_degree() + 1)


def distractor_2(polynomial):
    return str(polynomial.get_degree() - 1000)


def distractor_3(polynomial):
    return str(polynomial.get_degree() + 100)


def distractor_4(polynomial):
    if polynomial.get_degree != 0:
        return "0"


def distractor_5(polynomial):
    return "No such thing as a degree"


def test_polynomial():
    poly = Polynomial()
    print poly


def highest_degree(poly):
    polys = poly.split("+")
    polys = map(lambda x: x.replace("x^",""), polys)
    degrees = map(int, polys)
    return max(degrees)


def poly_random(values):
    polynomials = []
    for i in range(0,values['count']):
        poly1 = Polynomial()
        poly2 = Polynomial()
        poly3 = Polynomial()
        polynomial = str(poly1) + " + " + str(poly2) + " + " + str(poly3)
        polynomials.append(polynomial)
    return polynomials


# TODO - account for list of strings or other data types
def rand(values):
    return random.sample(range(values['start'], values['end']), values['count'])


functions = {'random': rand,'poly_random':poly_random}

"""Class to model a generate questions"""


# TODO - convert to moodle xml
class Question(object):
    def __init__(self, data, question_count=0):
        self.question_params = {}
        self.title = data['title']
        self.body = data['body']
        self.question_count = question_count
        self.answers = data['answer']
        self.distractors = data['distractor']
        self.build_question_params(data['params'])

    def build_question_params(self, params):
        list_params = None
        for k, v in params.iteritems():
            for key, value in v.iteritems():
                if value is None:
                    value = {}
                value['count'] = self.question_count
                list_params = functions[key](value)
            self.question_params[k] = list_params

    def gen_moodle_xml(self):
        params = {}
        for key, value in self.question_params.iteritems():
            try:
                params[key] = value.pop()
            except IndexError as e:
                print e
        print self.body.format(**params)
        print "********Options*********"

        # TODO - Handle multiple blocks to be evaluated
        for answer in self.answers:
            start_index = answer.index('$')
            end_index = answer.index('$', start_index + 1) + 1
            substr = answer[start_index:end_index]

            eval_block = substr[1:len(substr) - 1]
            eval_block = eval_block.format(**params)
            print answer.replace(substr, str(eval(eval_block)))
        for distractor in self.distractors:
            start_index = distractor.index('$')
            end_index = distractor.index('$', start_index + 1) + 1
            substr = distractor[start_index:end_index]

            eval_block = substr[1:len(substr) - 1]
            eval_block = eval_block.format(**params)
            print distractor.replace(substr, str(eval(eval_block)))


def test():
    print "Hello World"


def build_moodle_xml(yml_file=None, question=None, number_of_questions=50):
    with open(yml_file, 'r') as stream:
        try:
            dict_value = yaml.load(stream)
            if question is not None:
                question = Question(dict_value[question], number_of_questions)
                print "--------Question Data--------"
                for i in range(0, number_of_questions):
                    question.gen_moodle_xml()
                print "-----------------------------"
            else:
                print dict_value
        except yaml.YAMLError as exc:
            print(exc)
