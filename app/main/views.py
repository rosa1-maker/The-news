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
    render_template('index.html')