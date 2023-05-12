FUNC_PROTO = """\
#include "vendor/unity.h"

extern int is_pangram(const char *str);
"""

def gen_func_body(prop, inp, expected):
    sentence = inp["sentence"].replace('"', "\\\"")
    return (
        f'TEST_ASSERT_TRUE({prop}("{sentence}"));\n'
        if expected
        else f'TEST_ASSERT_FALSE({prop}("{sentence}"));\n'
    )
