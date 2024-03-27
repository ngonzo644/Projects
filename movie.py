import requests

class Movie:
    
    def __init__(self,s,key):
        """
        Creates a movie object to find a movie adaptation

        Args:
            s (str): The search for the movie
            key (str): The OMDb api key
        """
        self.key=key
        self.url=f'http://www.omdbapi.com/?s={s}&apikey={self.key}'
        self.movie=""
        self.year=""
        self.director=""
        self.adaptation=False
        
    def __str__(self):
        """
        Turns the movie object's values into a string

        Returns:
            str: All the variables of a movie object
        """
        return f'Key={self.key}, URL={self.url}, Movie={self.movie}, Year={self.year}, Director={self.director}, Adaptation={self.adaptation}'
    
    def get(self):
        """
        Based off the book that comes from the google books api, the get for OMDb api
        will use the given book name to find the first movie with the same name, which is the movie adaptation.

        Returns:
            self.movie(str): The movie found based off the book name
            self.year(str): The year the movie was released
            self.adaptation(bool): True if an adaptation is found, false otherwise.
            self.director(str): The director of the found movie
        """
        r=requests.get(self.url)
        if(r.status_code==200):
            response=r.json()
            if 'Search' in response:
                self.adaptation=True
                movie_info=response['Search']
                for movie in movie_info:
                    self.movie=movie['Title']
                    self.year=movie['Year']
                    self.more_info(movie)
                    break
            else:
                print("No match")
   
        return self.movie, self.year, self.adaptation, self.director
        
    
    def more_info(self,movie):
        """
        In order to find the directors name, this function further searches the OMDb api 
        with the movie's ImdbID to find more information
        
        Args:
            movie : used to traverse the json response that holds the movie's info
        """
        if 'imdbID' in movie:
            self.id=movie['imdbID']
            more_url=f'http://www.omdbapi.com/?i={self.id}&apikey={self.key}'
            response2=requests.get(more_url)
            more_data=response2.json()
            self.director=more_data['Director']
        

    