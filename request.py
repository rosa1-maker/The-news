import urllib.request,json
from models import News


api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url1
    api_key = app.config['MOVIE_API_KEY']
    basse_url = app.config['MOVIE_API_BASE_URL']
    