from newsapi import NewsApiClient
import pydoc

api_key=''

newsapi = NewsApiClient(api_key=api_key)

query=['Linux','Open-source','Android']
for i in query:
    all_articles = newsapi.get_everything(q=i,sort_by='publishedAt',page=1)
    all_articles=all_articles['articles']
    output=str()
    for j in all_articles:
        output+="title: {}\n - author: {}\n - date: {}\n - description:{}\n - url: {}\n\n".format(j['title'],j['author'],j['publishedAt'],j['description'],j['url'])
    pydoc.pager(output)
