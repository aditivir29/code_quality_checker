import matplotlib.pyplot as plt


def visualize_bar_chart(pep8_result, syntax_result):
    labels = ["PEP8 Violations", "Syntax Errors"]
    values = [pep8_result.get("violations", 0), syntax_result.get("errors", 0)]

    plt.bar(labels, values, color=["blue", "red"], alpha=0.7)
    plt.ylabel("Count")
    plt.title("Code Issues Overview")
    plt.show()


def visualize_pie_chart(pep8_result, syntax_result):
    labels = ["PEP8 Violations", "Syntax Errors"]
    values = [pep8_result.get("violations", 0), syntax_result.get("errors", 0)]

    if sum(values) == 0:
        print("✅ No issues to visualize.")
        return

    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140,
            colors=["skyblue", "salmon"])
    plt.title("Issue Distribution")
    plt.show()


def visualize_issues(pep8_result, syntax_result):
    visualize_bar_chart(pep8_result, syntax_result)
    visualize_pie_chart(pep8_result, syntax_result)
