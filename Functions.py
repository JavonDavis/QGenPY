def foo(values):
    x = values['foo_arg']
    return foo_helper(0, 1, x)


def foo_helper(p, q, r):
    if q > r:
        return 0
    else:
        return p + foo_helper(q, q + 1, r)


def foo_distractor(values):
    x = values['foo_arg']
    return foo_helper(0, 1, x+1)

