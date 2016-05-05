import random

"""All built in functions source code should be written in this file"""


# TODO - account for list of strings or other data types
def randrange(values):
    return random.sample(range(values['start'], values['end']), values['count'])


def make_set(values):
    return values['value'].split(",")


def randint(values):
    return random.randint(values['start'], values['end'])


# TODO - pick a random value from a parameter
def params(values):
    pass


# TODO - pick a ramdom value from a random parameter except these specified
def params_except(values):
    pass

built_in_functions = {'randrange': randrange, 'set': make_set, 'randint': randint, }