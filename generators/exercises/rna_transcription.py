FUNC_PROTO = """\
#include "vendor/unity.h"

#define BUFFER_SIZE 256

extern void to_rna(const char *strand, char *buffer);
"""

def gen_func_body(prop, inp, expected):
    dna = inp["dna"]
    str_list = [
        "char buffer[BUFFER_SIZE];\n\n",
        f'{prop}("{dna}", buffer);\n',
        f'TEST_ASSERT_EQUAL_STRING("{expected}", buffer);\n',
    ]
    return "".join(str_list)
