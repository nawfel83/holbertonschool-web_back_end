# python_variable_annotations/1-main.py
#!/usr/bin/env python3
"""Main file for testing concat function."""

concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
