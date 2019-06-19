from django.shortcuts import render,redirect
from . models import userProfile,News
import requests
from bs4 import BeautifulSoup
import json
from datetime import timedelta, timezone, datetime
import os
import shutil
import math

from django.views import generic
# Create your views here.

def scrape(request):
    News.objects.all().delete()
    #user_p = userProfile.objects.filter(user=request.user).first()
    #user_p.last_scrape = datetime.now(timezone.utc)
    #user_p.save()

    url = 'https://inshorts.com/en/read'
    response = requests.get(url)
    response_text = response.text
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    articlebody = soup.find_all(attrs = {"itemprop": "articleBody"})
    author = soup.find_all(attrs = {"class": "author"})
    datemonth = soup.find_all(attrs = {"class": "date"})
    for i in range(0,len(list(headlines))):
        headline = headlines[i].text
        body = articlebody[i].text
        auth = author[2*i].text
        date = datemonth[i].text

        new_news = News()
        new_news.headline = headline
        new_news.text = body
        new_news.author = auth
        new_news.datemonth = date
        new_news.save()
    return redirect('/index/')

def index(request):
    news = News.objects.all()
    context = {
        "object_list":news
    }
    return render(request,'index.html',context = context)