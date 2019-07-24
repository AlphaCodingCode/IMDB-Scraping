
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

# Main Function for scraping
def main(genre):


    urlIMDB = "https://www.imdb.com/search/title/?genres="+genre
    # HTTP request to get the data of
    # the whole page
    response = HTTP.get(urlIMDB)
    data = response.text

    # Parsing the data using
    # BeautifulSoup
    soup = SOUP(data, "lxml")

    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title

# Driver Function
if __name__ == '__main__':

    genre = raw_input("Enter a genre: ")
    a = main(genre)
    count = 0
    genre=genre.lower()


    for i in a:

        # Splitting each line of the
        # IMDb data to scrape movies
        tmp = str(i).split('</a>')
        if(len(tmp) == 2):
            tmp =tmp[0].split ('>')
            if(len(tmp) == 2):
                print(tmp[1])
                count += 1
        if(count > 10):
            break


