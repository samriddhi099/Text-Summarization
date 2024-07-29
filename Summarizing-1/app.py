from flask import Flask, render_template, request
from textsummary import summarizer
from abssummary import gen_abs_summary

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    if request.method == "POST":
        rawtext = request.form["rawtext"]
        summary, original_text, len_original_text, len_summary = summarizer(rawtext)

    return render_template(
        "summary.html",
        summary=summary,
        original_text=original_text,
        len_original_text=len_original_text,
        len_summary=len_summary
    )


@app.route("/analysis2", methods=["GET", "POST"])
def analysis2():
    if request.method == "POST":
        rawtext = request.form["rawtext"]
        summary, original_text, len_original_text, len_summary = gen_abs_summary(
            rawtext
        )

    return render_template(
        "summary2.html",
        summary=summary,
        original_text=original_text,
        len_original_text=len_original_text,
        len_summary=len_summary,
    )


if __name__ == "__main__":
    app.run(debug=True)
