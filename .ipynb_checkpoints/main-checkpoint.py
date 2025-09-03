import os
from src.pep8_checker import check_pep8
from src.syntax_checker import check_syntax
from src.scoring import calculate_score
from src.suggestions import generate_suggestions
from src.visualizer import visualize_issues
from src.report_generator import save_report, save_html_report
from src.features import analyze_complexity

# -----------------------
# Step 1: File to analyze
# -----------------------
filepath = "data/sample.py"
print(f"📂 Analyzing file: {filepath}")

# -----------------------
# Step 2: PEP8 & Syntax
# -----------------------
pep8_result = check_pep8(filepath)
syntax_result = check_syntax(filepath)
score = calculate_score(pep8_result, syntax_result)
suggestions = generate_suggestions(pep8_result, syntax_result)

print("\n=== Analysis Results ===")
print(f"PEP8 Violations: {pep8_result['violations']}")
print(f"Syntax Errors: {syntax_result['errors']}")
print(f"Score: {score}/10")

if suggestions:
    print("\n=== Suggestions ===")
    for s in suggestions:
        print("👉", s)
else:
    print("\n✅ No suggestions needed. Code looks clean!")

# -----------------------
# Step 3: Visualization
# -----------------------
print("\n📊 Generating visualizations...")
visualize_issues(pep8_result, syntax_result)

# -----------------------
# Step 4: Save Reports
# -----------------------
os.makedirs("reports", exist_ok=True)
report_data = {
    "pep8": pep8_result,
    "syntax": syntax_result,
    "score": score,
    "suggestions": suggestions
}
json_path = save_report("reports/analysis_report.json", report_data)
html_path = save_html_report("reports/analysis_report.html", report_data, pep8_result, syntax_result)
print(f"\n✅ JSON report saved at: {json_path}")
print(f"✅ HTML report saved at: {html_path}")

# -----------------------
# Step 5: Complexity Analysis
# -----------------------
print("\n=== Cyclomatic Complexity & Maintainability Index ===")
if syntax_result["errors"] > 0:
    print("⏩ Skipping complexity analysis due to syntax errors.")
else:
    complexity_result = analyze_complexity(filepath)

    if "error" in complexity_result:
        print(f"⏩ Complexity analysis error: {complexity_result['error']}")
    else:
        cc_list = complexity_result.get("cyclomatic_complexity", [])
        for func in cc_list:
            warning = " ⚠️ High complexity!" if func['complexity'] > 10 else ""
            print(f"Function {func['name']} (line {func['lineno']}): Complexity = {func['complexity']}{warning}")

        print(f"\nMaintainability Index: {complexity_result['maintainability_index']:.2f}")

# -----------------------
# Step 6: Final Summary
# -----------------------
print("\n=== Final Summary ===")
print(f"📂 File: {filepath}")
print(f"🔹 PEP8 Violations: {pep8_result['violations']}")
print(f"🔹 Syntax Errors: {syntax_result['errors']}")
print(f"🔹 Score: {score}/10")
if complexity_result and "error" not in complexity_result:
    print(f"🔹 Cyclomatic Complexity:")
    for func in cc_list:
        warning = " ⚠️ High complexity!" if func['complexity'] > 10 else ""
        print(f"    • {func['name']} (line {func['lineno']}): {func['complexity']}{warning}")
    print(f"🔹 Maintainability Index: {complexity_result['maintainability_index']:.2f}")
else:
    print("🔹 Complexity analysis skipped or failed due to errors.")

# -----------------------
# Step 7: Save Complexity in Report
# -----------------------
report_data["complexity"] = complexity_result
save_report("reports/analysis_report.json", report_data)
save_html_report("reports/analysis_report.html", report_data, pep8_result, syntax_result)
