from qgen import functions

"""Helper functions that are essential to the construction of questions"""


def evaluate_blocks(text, params):
    """Evaluates the code blocks delimited by a $ in a question's answer or distractor"""
    while "$" in text:
        start_index = text.index('$')
        end_index = text.index('$', start_index + 1) + 1

        # get code to be evaluated
        substr = text[start_index:end_index]

        # remove leading and trailing $
        eval_block = substr[1:len(substr) - 1]

        # fill in arguments
        eval_block = eval_block.format(**params)
        text = text.replace(substr, str(eval(eval_block)))
    return text


def evaluate_functions(text, params):
    """Evaluates the functions delimited by a @ in a question's answer or distractor"""
    while "@" in text:
        start_index = text.index('@')
        end_index = text.index('@', start_index + 1) + 1
        substr = text[start_index:end_index]

        eval_block = substr[1:len(substr) - 1]
        # find function
        function_name = eval_block[:eval_block.index("(")]
        # find arguments

        text = text.replace(substr, str(functions[function_name](params)))
    return text


def evaulate_braces(text,params):
    while "[" in text:
        start_index = text.index('[')
        end_index = text.index(']',start_index + 1) + 1
        substr = text[start_index:end_index]

        choices = substr.split(",")