import pycodestyle


def check_pep8(file_path):
    """
    Run PEP8 (pycodestyle) checks on a file.
    Returns dict with violation count and details.
    """
    style_guide = pycodestyle.StyleGuide(quiet=False)
    report = style_guide.check_files([file_path])

    violations = report.total_errors
    details = []

    # Extract statistics of errors/warnings
    for stat in report.get_statistics("E"):  # Errors
        details.append(stat)
    for stat in report.get_statistics("W"):  # Warnings
        details.append(stat)

    return {
        "violations": violations,
        "details": details
    }
