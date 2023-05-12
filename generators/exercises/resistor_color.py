FUNC_PROTO = """\
#include "vendor/unity.h"

#define ARRAY_SIZE(x) (sizeof(x) / sizeof((x)[0]))

extern int color_code(const char *color);
extern const char **colors(void);
"""

def gen_func_body(prop, inp, expected):
    str_list = []
    if prop == "color_code":
        color = inp["color"]
        str_list.append(f'TEST_ASSERT_EQUAL_INT({expected}, {prop}("{color}"));\n')
    elif prop == "colors":
        color_array = str(expected).replace("'", '"')
        color_array = color_array.replace("[", "{")
        color_array = color_array.replace("]", "}")
        str_list.extend(
            (
                f"const char **color_array = {prop}();\n",
                f"const char *expected[] = {color_array};\n",
                "int size;\n\n",
                "for (size = 0; color_array[size]; size++) {\n",
                "}\n",
                "TEST_ASSERT_EQUAL_INT(ARRAY_SIZE(expected), size);\n",
                "TEST_ASSERT_EQUAL_STRING_ARRAY(expected, color_array, size);\n",
            )
        )
    return "".join(str_list)
