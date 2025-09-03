import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import os


def save_report(file_path, report_data):
    """
    Save analysis results into a JSON file.
    """
    with open(file_path, "w") as f:
        json.dump(report_data, f, indent=4)
    return file_path


def _fig_to_base64(fig):
    """Convert a matplotlib figure to base64 string."""
    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode("utf-8")
    plt.close(fig)
    return img_str


def save_html_report(file_path, report_data, pep8_result, syntax_result):
    """
    Save analysis results into an HTML report with charts.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # --- Generate bar chart ---
    fig1, ax1 = plt.subplots()
    ax1.bar(["PEP8 Violations", "Syntax Errors"],
            [pep8_result.get("violations", 0), syntax_result.get("errors", 0)],
            color=["blue", "red"], alpha=0.7)
    ax1.set_ylabel("Count")
    ax1.set_title("Code Issues Overview")
    bar_chart = _fig_to_base64(fig1)

    # --- Generate pie chart ---
    fig2, ax2 = plt.subplots()
    values = [pep8_result.get("violations", 0), syntax_result.get("errors", 0)]
    labels = ["PEP8 Violations", "Syntax Errors"]
    if sum(values) > 0:
        ax2.pie(values, labels=labels, autopct="%1.1f%%", startangle=140,
                colors=["skyblue", "salmon"])
        ax2.set_title("Issue Distribution")
        pie_chart = _fig_to_base64(fig2)
    else:
        pie_chart = None

    # --- Build HTML ---
    html_content = f"""
    <html>
    <head>
        <title>Code Quality Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            .section {{ margin-bottom: 20px; }}
            img {{ max-width: 600px; border: 1px solid #ccc; padding: 5px; }}
            ul {{ line-height: 1.6; }}
        </style>
    </head>
    <body>
        <h1>📊 Code Quality Report</h1>
        <div class="section">
            <h2>Summary</h2>
            <p><b>Score:</b> {report_data['score']}/10</p>
            <p><b>PEP8 Violations:</b> {pep8_result['violations']}</p>
            <p><b>Syntax Errors:</b> {syntax_result['errors']}</p>
        </div>

        <div class="section">
            <h2>Suggestions</h2>
            <ul>
                {''.join(f"<li>{s}</li>" for s in report_data['suggestions'])}
            </ul>
        </div>

        <div class="section">
            <h2>Visualizations</h2>
            <h3>Bar Chart</h3>
            <img src="data:image/png;base64,{bar_chart}" />
            {"<h3>Pie Chart</h3><img src='data:image/png;base64," + pie_chart + "' />" if pie_chart else "<p>No issues to display in pie chart.</p>"}
        </div>
    </body>
    </html>
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return file_path
