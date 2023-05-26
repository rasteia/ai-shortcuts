import ast

## SecurityChecker.py: A tool that checks for common security vulnerabilities in python code.

class SecurityChecker(ast.NodeVisitor):
    def __init__(self):
        self.vulnerabilities = []

    def check_vulnerabilities(self, code):
        tree = ast.parse(code)
        self.visit(tree)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            function_name = node.func.id
            if function_name in ['exec', 'eval']:
                vulnerability = {
                    'type': 'Dangerous Function',
                    'line': node.lineno,
                    'message': f'Use of dangerous function: {function_name}'
                }
                self.vulnerabilities.append(vulnerability)

        self.generic_visit(node)

    # Add more visit methods for other vulnerability checks as needed

    def get_vulnerabilities(self):
        return self.vulnerabilities


if __name__ == '__main__':
    # Example usage
    code_to_check = """
    user_input = input("Enter your name: ")
    exec(user_input)
    """

    checker = SecurityChecker()
    checker.check_vulnerabilities(code_to_check)
    vulnerabilities = checker.get_vulnerabilities()

    if vulnerabilities:
        print("Vulnerabilities found:")
        for vulnerability in vulnerabilities:
            print(f" - {vulnerability['type']} at line {vulnerability['line']}: {vulnerability['message']}")
    else:
        print("No vulnerabilities found.")
