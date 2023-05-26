import re
## UserInputChecker.py: A tool that checks for common security vulnerabilities in user input fields.
def check_sql_injection(script):
    sql_pattern = re.compile(r"(?:\b|\")SELECT\b.*?\bFROM\b.*?(?:\bWHERE\b|\")", re.IGNORECASE)
    matches = re.findall(sql_pattern, script)
    if matches:
        print("Potential SQL injection found:")
        for match in matches:
            print(match)

def check_xss(script):
    xss_pattern = re.compile(r"(?:<|&lt;)(?:script|img|on\w+).*?(?:>|&gt;)", re.IGNORECASE)
    matches = re.findall(xss_pattern, script)
    if matches:
        print("Potential XSS vulnerability found:")
        for match in matches:
            print(match)

def check_command_injection(script):
    command_pattern = re.compile(r"(?:os\.\w+|subprocess\.\w+)\((.*?)\)")
    matches = re.findall(command_pattern, script)
    if matches:
        print("Potential command injection found:")
        for match in matches:
            print(match)

def check_path_traversal(script):
    path_pattern = re.compile(r"(?:\.\.[\\/])+")
    matches = re.findall(path_pattern, script)
    if matches:
        print("Potential path traversal found:")
        for match in matches:
            print(match)

def check_deserialization(script):
    deserialization_pattern = re.compile(r"pickle\.load\((.*?)\)")
    matches = re.findall(deserialization_pattern, script)
    if matches:
        print("Potential deserialization vulnerability found:")
        for match in matches:
            print(match)

# Example usage
if __name__ == "__main__":
    with open("target_script.py", "r") as file:
        script_content = file.read()

    check_sql_injection(script_content)
    check_xss(script_content)
    check_command_injection(script_content)
    check_path_traversal(script_content)
    check_deserialization(script_content)
