"""Flask server for the Sentiment Analysis web application."""

from flask import Flask, render_template, request
from SentimentAnalysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyze the sentiment of the text received from the web interface.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)

    if response["label"] is None:
        return "Invalid input ! Try again."

    return (
        f"The given text has been identified as "
        f"{response['label']} with a score of {response['score']}."
    )


@app.route("/")
def render_index_page():
    """
    Render the application's home page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
