import yaml
import random
import moodle_xml_builder as mxb
import importlib

# TODO - account for list of strings or other data types
def rand(values):
    return random.sample(range(values['start'], values['end']), values['count'])

functions = {'random': rand}

"""Class to model a generate questions"""

# TODO - convert to moodle xml
class Question(object):
    def __init__(self, data, question_count=0):
        self.question_params = {}
        self.title = data['title']
        self.type = data['type']
        self.body = data['body']
        self.question_count = question_count
        self.answers = data['answer']
        self.add_imports(data)
        self.distractors = data['distractor']
        self.build_question_params(data['params'])

    def add_imports(self, data):
        if 'imports' in data:
            imports = data['imports']
            for name, source in imports.iteritems():
                try:
                    functions[name] = importlib.import_module(source).__getattribute__(name)
                except AttributeError:
                    pass # log it

    def build_question_params(self, params):
        list_params = None
        for parameter_name, function_name in params.iteritems():
            for function_param, arguments in function_name.iteritems():
                if arguments is None:
                    arguments = {}
                arguments['count'] = self.question_count
                list_params = functions[function_param](arguments)
            self.question_params[parameter_name] = list_params

    def gen_moodle_xml(self):
        params = {}
        for key, value in self.question_params.iteritems():
            try:
                params[key] = value.pop()
            except IndexError as e:
                print e
        print self.body.format(**params)
        print "********Options*********"

        body_for_xml = self.body.format(**params)
        mxb.build_question_for_xml(self.title, body_for_xml, self.type)

        for answer in self.answers:
            while "$" in answer:
                start_index = answer.index('$')
                end_index = answer.index('$', start_index + 1) + 1
                substr = answer[start_index:end_index]

                eval_block = substr[1:len(substr) - 1]
                eval_block = eval_block.format(**params)
                answer = answer.replace(substr, str(eval(eval_block)))
            while "@" in answer:
                start_index = answer.index('@')
                end_index = answer.index('@', start_index + 1) + 1
                substr = answer[start_index:end_index]

                eval_block = substr[1:len(substr) - 1]
                #find function
                function_name = eval_block[:eval_block.index("(")]
                #find arguments
                arguments = eval_block[eval_block.index("(")+1:eval_block.index(")")]
                arguments = arguments.replace("{", "")
                arguments = arguments.replace("}", "")
                arguments = params[arguments] #This doesn't work for multiple arguments
                #evaluate and replace string
                answer = answer.replace(substr, str(functions[function_name](arguments)))
                print answer
            mxb.build_answer_for_xml(answer)
            print answer
        for distractor in self.distractors:
            while "$" in distractor:
                start_index = distractor.index('$')
                end_index = distractor.index('$', start_index + 1) + 1
                substr = distractor[start_index:end_index]

                eval_block = substr[1:len(substr) - 1]
                eval_block = eval_block.format(**params)
                distractor = distractor.replace(substr, str(eval(eval_block)))
                mxb.build_answer_for_xml(distractor)
            while "@" in distractor:
                start_index = distractor.index('@')
                end_index = distractor.index('@', start_index + 1) + 1
                substr = distractor[start_index:end_index]

                eval_block = substr[1:len(substr) - 1]
                eval_block = eval_block.format(**params)
                eval_block = substr[1:len(substr) - 1]
                #find function
                function_name = eval_block[:eval_block.index("(")]
                #find arguments
                arguments = eval_block[eval_block.index("(")+1:eval_block.index(")")]
                arguments = arguments.replace("{", "")
                arguments = arguments.replace("}", "")
                arguments = params[arguments] #This doesn't work for multiple arguments
                #evaluate and replace string
                distractor = distractor.replace(substr, str(functions[function_name](arguments)))
                mxb.build_answer_for_xml(distractor)
            print distractor
        mxb.build_question_end_tag()


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
