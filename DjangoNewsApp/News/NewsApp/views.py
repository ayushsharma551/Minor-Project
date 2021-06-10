from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.



def Index(request):
    newsapi = NewsApiClient(api_key="1f2dc5dfb16a43a2b9e37fc3d8c7bb6b")


    #topheadlines = newsapi.get_top_headlines(sources="google-news")
    topheadlines = newsapi.get_top_headlines(q='covid',
                                          sources='bbc-news,the-verge,cnn,'
                                          )



    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur= []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])

    mylist = zip(news, desc, img, ur)

    return render(request, 'index.html', context={"mylist":mylist})