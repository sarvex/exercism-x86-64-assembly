FUNC_PROTO = """\
#include "vendor/unity.h"

#define BUFFER_SIZE 256

extern void rotate(const char *text, int shift_key, char *buffer);
"""

def gen_func_body(prop, inp, expected):
    text = inp["text"]
    shift_key = inp["shiftKey"]
    str_list = [
        "char buffer[BUFFER_SIZE];\n\n",
        f'{prop}("{text}", {shift_key}, buffer);\n',
        f'TEST_ASSERT_EQUAL_STRING("{expected}", buffer);\n',
    ]
    return "".join(str_list)
