from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_articles
from ..models import Review

@main.route('/')
def index():
	'''
    It returns the index page and its content

	'''
	news =get_news('category', 'api_key')
	print(news)

	
	business_news= get_news('business')
	sports_news = get_news('sports')
	technology_news = get_news('technology')
	entertainment_news = get_news('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title, business_news =business_news, sports_news = sports_news,technology_news = technology_news,entertainment_news = entertainment_news)


@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'News | {id}'

	return render_template('articles.html',title= title,articles = articles)
