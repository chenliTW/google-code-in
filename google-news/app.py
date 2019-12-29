from newsapi import NewsApiClient
import pydoc
import pprint

api_key='9ebb83fde9d84aa2bf624dcc350179c5'

newsapi = NewsApiClient(api_key=api_key)

query=['Linux','','']
for i in query:
    all_articles = newsapi.get_everything(q=i,sort_by='publishedAt',page=1)
    all_articles=all_articles['articles']
    output=str()
    pprint.pprint(all_articles)
    for j in all_articles:
        output+="title: {}\ndate: {}\ncontent:{}".format(j['title'],j['publishedAt'],j['description'])
    pydoc.pager(output)
