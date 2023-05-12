FUNC_PROTO = """\
#include "vendor/unity.h"

extern int is_isogram(const char *str);
"""

def gen_func_body(prop, inp, expected):
    phrase = inp["phrase"]
    return (
        f'TEST_ASSERT_TRUE({prop}("{phrase}"));\n'
        if expected
        else f'TEST_ASSERT_FALSE({prop}("{phrase}"));\n'
    )
