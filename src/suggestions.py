def generate_suggestions(pep8_result, syntax_result):
    """
    Generate human-readable suggestions based on PEP8 and syntax issues.
    """
    suggestions = []

    # Syntax error suggestions
    for err in syntax_result.get("details", []):
        suggestions.append(
            f"Line {err['line']}: {err['msg']} – Hint: {err['hint']}"
        )

    # PEP8 style suggestions
    if pep8_result["violations"] > 0:
        suggestions.append("Fix PEP8 style issues using autopep8 or black.")
        for detail in pep8_result.get("details", []):
            suggestions.append(f"PEP8: {detail}")

    if not suggestions:
        suggestions.append("✅ Code looks clean and follows best practices!")

    return suggestions
