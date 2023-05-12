FUNC_PROTO = """\
#include "vendor/unity.h"

extern void reverse(char *str);
"""

def gen_func_body(prop, inp, expected):
    value = inp["value"]
    str_list = [
        f'char str[] = "{value}";\n\n',
        f'{prop}(str);\n',
        f'TEST_ASSERT_EQUAL_STRING("{expected}", str);\n',
    ]
    return "".join(str_list)
