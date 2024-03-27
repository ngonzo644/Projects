import requests

class Book:
    def __init__(self,q,key):
        """
        Creates a book object with a url, title, and author

        Args:
            q (str): The book the user wants to find
            key (str): The google books api key
        """
        self.url=f'https://www.googleapis.com/books/v1/volumes?q={q}&key={key}'
        self.title=""
        self.author=""
        
    def __str__(self):
        """
        The variables of a book object put into a string

        Returns:
            str: A book object's variables
        """
        return f'URL={self.url}, Title={self.title}, Author={self.author}'
        
    def get(self):
        """
        finds a book using the google books api, along with the authors name.

        Returns:
            self.title(str): The title of the book
            self.author(str): the author of the book
        """
        r=requests.get(self.url)
        if r.status_code==200:
            response=r.json()
            if 'items' in response:
                book_info=response['items'][0]['volumeInfo']
                self.title=book_info['title']
                self.author=book_info['authors'][0]
            else:
                print("No books found")
        return self.title, self.author
        

