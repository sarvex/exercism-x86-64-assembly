FUNC_PROTO = """\
#include "vendor/unity.h"

extern int leap_year(int year);
"""

def gen_func_body(prop, inp, expected):
    year = inp["year"]
    return (
        f"TEST_ASSERT_TRUE({prop}({year}));\n"
        if expected
        else f"TEST_ASSERT_FALSE({prop}({year}));\n"
    )
