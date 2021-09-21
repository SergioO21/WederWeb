#!/usr/bin/python3
"""  """

from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route("/")
def index():
    news_api = NewsApiClient(api_key="c42f265031af41b790afbfb93a04d0a9")
    top_headlines = news_api.get_top_headlines(sources="bbc-news")

    articles = top_headlines["articles"]

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        my_articles = articles[i]

        news.append(my_articles["title"])
        desc.append(my_articles["description"])
        img.append(my_articles["urlToImage"])

    my_list = zip(news, desc, img)
    return render_template("index.html", context=my_list)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
