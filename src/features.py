import radon.complexity as radon_cc
from radon.metrics import mi_visit
import ast
import pandas as pd

def analyze_complexity(file_path):
    """
    Analyze cyclomatic complexity (CC) and maintainability index (MI).
    Returns a dictionary with detailed results.
    """
    try:
        with open(file_path, "r") as f:
            source = f.read()
    except Exception as e:
        return {"error": f"Could not read file: {e}"}

    try:
        # Cyclomatic Complexity
        cc_results = radon_cc.cc_visit(source)
        cc_data = [
            {
                "name": item.name,
                "lineno": item.lineno,
                "complexity": item.complexity
            }
            for item in cc_results
        ]

        # Maintainability Index
        mi_score = mi_visit(source, True)

        return {
            "cyclomatic_complexity": cc_data,
            "maintainability_index": mi_score
        }
    except SyntaxError:
        return {"error": "Syntax error – skipping complexity analysis."}
    except Exception as e:
        return {"error": str(e)}


def print_complexity_report(complexity_result):
    """
    Nicely prints cyclomatic complexity and maintainability index.
    """
    if "error" in complexity_result:
        print(f"⏩ Skipping complexity analysis: {complexity_result['error']}")
        return

    print("\n=== Cyclomatic Complexity ===")
    if complexity_result["cyclomatic_complexity"]:
        for item in complexity_result["cyclomatic_complexity"]:
            print(f"Function {item['name']} (line {item['lineno']}): "
                  f"Complexity = {item['complexity']}")
    else:
        print("No functions found.")

    print(f"\nMaintainability Index: {complexity_result['maintainability_index']:.2f}")
