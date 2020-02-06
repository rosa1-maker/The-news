class News:
    '''
    A news class to define the news  objective
    '''

    def __init__(self, id,name,description,url,category,country,language):
        self.id =id
        self.name =name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language


class Article:
    
    def __init__(self, id,author,title,description,url,urlToImage,publishedAt):
        self.id =id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        



