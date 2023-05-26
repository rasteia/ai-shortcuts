import ast
import sys

## CodeReview.py: a Python script that analyzes other Python files and checks for common issues based on a coding checklist. 

def analyze_file(filename):
    try:
        with open(filename, 'r') as file:
            source = file.read()
            tree = ast.parse(source)
            issues = check_for_issues(tree)
            if issues:
                print(f"Issues found in file: {filename}")
                for issue in issues:
                    print(f"- {issue}")
            else:
                print(f"No issues found in file: {filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except IOError:
        print(f"Error reading file: {filename}")


def check_for_issues(tree):
    issues = []
    issues.extend(check_indentation(tree))
    issues.extend(check_unused_variables(tree))
    issues.extend(check_function_length(tree))
    issues.extend(check_variable_naming(tree))
    issues.extend(check_magic_methods(tree))
    issues.extend(check_imports(tree))
    return issues


def check_function_length(tree, max_lines=50):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            lines = node.body[-1].end_lineno - node.lineno
            if lines > max_lines:
                issues.append(f"Function '{node.name}' exceeds {max_lines} lines")
    return issues


def check_variable_naming(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Name) and not subnode.id.startswith('_'):
                    if not subnode.id.islower() and not subnode.id.isupper() and not subnode.id.isidentifier():
                        issues.append(f"Invalid variable name '{subnode.id}' in line {subnode.lineno}")
    return issues


def check_magic_methods(tree):
    issues = []
    magic_methods = {
        '__init__': 1,
        '__del__': 1,
        '__str__': 1,
        '__repr__': 1,
        '__eq__': 2,
        '__lt__': 2,
        '__gt__': 2,
        '__len__': 1,
        '__getitem__': 2,
        '__setitem__': 3,
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name in magic_methods:
                args_count = len(node.args.args) - len(node.args.defaults or [])
                if args_count != magic_methods[node.name]:
                    issues.append(f"Invalid number of arguments in magic method '{node.name}' in line {node.lineno}")
    return issues


def check_imports(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name.startswith('_'):
                    issues.append(f"Invalid import '{alias.name}' in line {node.lineno}")
    return issues



def check_indentation(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if node.body and not isinstance(node.body[0], ast.Expr):
                if not isinstance(node.body[0], ast.Pass):
                    if node.body[0].col_offset != 4:
                        issues.append(f"Indentation error in line {node.lineno}")
    return issues


def check_unused_variables(tree):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            defined_variables = set()
            used_variables = set()
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Name):
                    if isinstance(subnode.ctx, ast.Store):
                        defined_variables.add(subnode.id)
                    elif isinstance(subnode.ctx, ast.Load):
                        used_variables.add(subnode.id)
            unused_variables = defined_variables - used_variables
            if unused_variables:
                issues.append(f"Unused variables in function '{node.name}': {unused_variables}")
    return issues


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python CodeReview.py <filename>")
    else:
        filename = sys.argv[1]
        analyze_file(filename)
