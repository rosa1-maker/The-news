class News:
    '''
    A news class to define the news  objective
    '''

    def __init__(self, id, title, overview,poster,country,url,description,language):
        self.id =id
        self.title = title
        self.overview =overview
        self.poster = poster
        self.country = country
        self.url = url
        self.description = description
        self.language = language


class Review:
    all_reviews =[]        
    def __init__(self, news_id, title, imageurl,Review,description,date):
        self.news_id =news_id
        self.title = title
        self.imageurl = imageurl
        self.review =Review
        self.description = description
        self.date = date


    def save_the _reviews(self)
        review.all_reviews.append(self) 



    @classmethod
     def clear_the _reviews(cls)    
        Review.all_reviews.clear()

    @classmethod
    def get_the _reviews(cls,id):

        response =[] 

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response        
