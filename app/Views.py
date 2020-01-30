from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    It returns the index page and its content
    '''
    render_template('index.html')

