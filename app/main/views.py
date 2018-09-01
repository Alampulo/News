from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_articles, get_news


#views
@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = "Home || News Sources"

    all_news = get_news('sports')
    general_news = get_news('general')
    tech_news = get_news('technology')
    bus_news = get_news('business')
    sci_news = get_news('science')


    # print(all_news)


    return render_template('index.html', title= title, sports = all_news, general = general_news, technology = tech_news, business = bus_news, science = sci_news)
