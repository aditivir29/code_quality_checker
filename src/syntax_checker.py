import ast


def check_syntax(file_path):
    """
    Parse Python code to detect syntax errors.
    Returns dict with error count and details.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        ast.parse(source)
        return {"errors": 0, "details": []}
    except SyntaxError as e:
        return {
            "errors": 1,
            "details": [{
                "line": e.lineno,
                "msg": e.msg,
                "hint": "Check function/class definitions and missing colons/indentation."
            }]
        }
