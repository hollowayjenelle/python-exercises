import requests
import re
from bs4 import BeautifulSoup

def decode():
    r = requests.get("https://www.nytimes.com/") #gets the content of this webpage
    lst = []
    soup = BeautifulSoup(r.text, 'html.parser') #r.text gets the html of the webpage; beautifulsoup makes it possible to read and understand
    for i in soup.find_all(re.compile("^h")):   #finds all the tags that begin with h
       lst.append(i.string)

    print(lst)

if __name__ == '__main__':
    decode()

#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
#  New York Times homepage.