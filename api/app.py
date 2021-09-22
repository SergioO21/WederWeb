#!/usr/bin/python3
"""  """

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    api_key = "c42f265031af41b790afbfb93a04d0a9"
    country = "co"
    news_api_url = "https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(country, api_key)
    top_headlines = requests.get(news_api_url).json()

    articles = top_headlines["articles"]

    desc = []
    news = []
    img = []
    urls = []

    for i in range(len(articles)):
        my_articles = articles[i]

        news.append(my_articles["title"])
        desc.append(my_articles["description"])
        img.append(my_articles["urlToImage"])
        urls.append(my_articles["url"])

    my_list = zip(news, desc, img, urls)
    return render_template("index.html", context=my_list)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
