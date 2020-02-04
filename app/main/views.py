from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_news,get_news,search_news
from .forms import ReviewForm
from .models import Review

@main.route('/')
def index():
	'''
    It returns the index page and its content

	'''
	sources = get_sources('business')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	entertainment_sources = get_sources('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)


@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'News | {id}'

	return render_template('articles.html',title= title,articles = articles)
