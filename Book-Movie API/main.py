from book import Book
from movie import Movie

def main():
    """
    Asks' for input on what book the user would like to see is an adaptation. 
    Prints the movie information if found.
    
    """
    query=input("What book do you want to search for?")
    example=Book(query, "AIzaSyAm5Hq7hWZJkH0aDTK09eoa7UOyC55DNgI")

    title,author=example.get()

    print(f'Book:{title}, Author: {author}')

    example2=Movie(title,"ba4435be")

    title2, year, adaptation, director=example2.get()

    if(adaptation):
        print(f'Movie:{title2} {year}, Director: {director}')
        print("This is the adaptation!")
    
    
if __name__ == '__main__':
    main()
