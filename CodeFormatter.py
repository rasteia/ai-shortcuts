# CodeFormatter.py : A script that automatically formats code according to a specific style guide.
# This can be useful for maintaining consistency and readability in a project.

import re


class CodeFormatter:
    def __init__(self):
        self.indentation = "    "
        self.newline = "\n"

    def format_code(self, code):
        formatted_code = self.remove_trailing_whitespace(code)
        formatted_code = self.indent_code(formatted_code)
        formatted_code = self.add_newlines(formatted_code)
        formatted_code = self.add_spaces_around_operators(formatted_code)
        formatted_code = self.add_spaces_after_commas(formatted_code)
        formatted_code = self.remove_spaces_between_parentheses(formatted_code)
        return formatted_code

    def remove_trailing_whitespace(self, code):
        lines = code.split(self.newline)
        formatted_lines = [line.rstrip() for line in lines]
        return self.newline.join(formatted_lines)

    def indent_code(self, code):
        lines = code.split(self.newline)
        indent_level = 0
        formatted_lines = []

        for line in lines:
            line = line.strip()
            if line.endswith(":") or line.endswith("{") or line.endswith("["):
                indent_level += 1
            elif line.startswith("return") or line.startswith("pass") or line.startswith("break"):
                indent_level -= 1

            formatted_lines.append(self.indentation * indent_level + line)

        return self.newline.join(formatted_lines)

    def add_newlines(self, code):
        code = re.sub(r"(\n+)", self.newline, code)
        return code

    def add_spaces_around_operators(self, code):
        operators = ["=", "+", "-", "*", "/", "//", "%", "**", "==", "!=", "<", ">", "<=", ">=", "+=", "-=", "*=", "/=", "//=", "%=", "**="]
        for operator in operators:
            code = re.sub(r"(\S)" + re.escape(operator) + r"(\S)", r"\1 " + operator + r" \2", code)
        return code

    def add_spaces_after_commas(self, code):
        code = re.sub(r"(\S),", r"\1, ", code)
        return code

    def remove_spaces_between_parentheses(self, code):
        code = re.sub(r"\(\s+(.*?)\s+\)", r"(\1)", code)
        code = re.sub(r"\[\s+(.*?)\s+\]", r"[\1]", code)
        code = re.sub(r"\{\s+(.*?)\s+\}", r"{\1}", code)
        return code


# Example usage
if __name__ == "__main__":
    formatter = CodeFormatter()

    code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
"""

    formatted_code = formatter.format_code(code)
    print(formatted_code)
