from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles


#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and
    its data
    '''

    # getting the general sources
    sources = get_sources()
    print(sources)
    title = 'Home - Jumas Online News Website'
    return render_template('index.html',title=title,sources=sources)

@main.route('/news/<id>')
def news(id):
    '''
    view page function that returns the news articles and its data
    '''
    articles = get_articles(id)
    title = 'Home - Welcome to the best Online News Website'
    print(articles)
    return render_template('news.html', articles=articles, title=title)
