def calculate_score(pep8_result, syntax_result):
    """
    Simple scoring system (0–10 scale).
    - Deduct points for syntax errors (heavy penalty).
    - Deduct smaller penalties for PEP8 violations.
    """
    score = 10.0

    # Syntax errors are critical
    if syntax_result["errors"] > 0:
        score -= 2 * syntax_result["errors"]

    # PEP8 penalties
    score -= 0.1 * pep8_result["violations"]

    # Bound between 0 and 10
    return max(0, round(score, 1))
