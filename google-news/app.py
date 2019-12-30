from newsapi import NewsApiClient
from flask import Flask


api_key=''

newsapi = NewsApiClient(api_key=api_key)

app=Flask(__name__)

@app.route('/')
def index():
    query=['Linux','Open-source','Android']
    output="<html><body>"
    for i in query:
        output+="<details><summary>{}</summary>".format(i)
        all_articles = newsapi.get_everything(q=i,sort_by='publishedAt',page=1)
        all_articles=all_articles['articles']
        for j in all_articles:
            output+="<table border='1' width='100%'>"
            output+="<tr><th>{}</th></tr><tr><td> - author: {}</tr></td><tr><td> - date: {}</tr></td><tr><td> - description:{}</tr></td><tr><td> - url: <a href='{}'>full article link</a></tr></td>".format(j['title'],j['author'],j['publishedAt'],j['description'],j['url'])
            output+="</table>"
        output+="</details>"
    output+="</html></body>"
    return output

app.run()