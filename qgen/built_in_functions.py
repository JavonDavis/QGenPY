import random

"""All built in functions source code should be written in this file"""


def randrange(values):
    return random.sample(range(values['start'], values['end']), values['end'] - values['start'])


def make_set(values):
    return values['value'].split(",")


def randint(values):
    return random.randint(values['start'], values['end'])


built_in_functions = {'randrange': randrange, 'set': make_set, 'randint': randint, }