import os

class Config:

    NEW_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=b6607b89849d485b9d8eda17f4187dd6'
    MOVIE_API_KEY = os.environ.get('NEW_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass



class DevConfig(Config):
    DEBUG = True


config_options ={
    'development':DevConfig,
    'production' :ProdConfig
}