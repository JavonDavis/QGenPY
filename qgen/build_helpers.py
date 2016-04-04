from qgen import functions

"""Helper functions that are essential to the construction of questions"""


def evaluate_code_blocks(answer_distractor, params):
    """Evaluates the code blocks delimited by a $ in a question's answer or distractor"""
    while "$" in answer_distractor:
        start_index = answer_distractor.index('$')
        end_index = answer_distractor.index('$', start_index + 1) + 1
        substr = answer_distractor[start_index:end_index]

        eval_block = substr[1:len(substr) - 1]
        eval_block = eval_block.format(**params)
        answer_distractor = answer_distractor.replace(substr, str(eval(eval_block)))
    return answer_distractor


def evaluate_functions(answer_distractor, params):
    """Evaluates the functions delimited by a @ in a question's answer or distractor"""
    while "@" in answer_distractor:
        start_index = answer_distractor.index('@')
        end_index = answer_distractor.index('@', start_index + 1) + 1
        substr = answer_distractor[start_index:end_index]

        eval_block = substr[1:len(substr) - 1]
        # find function
        function_name = eval_block[:eval_block.index("(")]
        # find arguments
        arguments = eval_block[eval_block.index("(") + 1:eval_block.index(")")]
        arguments = arguments.replace("{", "")
        arguments = arguments.replace("}", "")
        arguments = params[arguments]  # This doesn't work for multiple arguments
        # evaluate and replace string
        answer_distractor = answer_distractor.replace(substr, str(functions[function_name](arguments)))
    return answer_distractor
