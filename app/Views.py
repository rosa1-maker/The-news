from flask import render_template

class Views()
@app.route('/')
def index():

    '''
    It returns the index page and its content
    '''
    render_template('index.html')

