"""
PE03's requirements:
Extract all the links from this website https://news.ycombinator.com/news 
Feel free to use whatever tools and techniques you prefer.

In the same file, after you successfully get titles and links, 
then save all those to text file or Excel file (your choice). 
The file should contain the name of each link and the link itself.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# This function is to scrape the news' titles and urls
# and export the information into a text file

# Since there are many pages in the given url, 
# we'll limit the number of request made to improve on performance, 
# as well as prevent getting our IP blocked from the server. 

def scrape_news(pages = 1):
    base_url = 'https://news.ycombinator.com/news'
    titles = []
    links = []
    
    for page in range(1, pages + 1): #limiting page to scrape, default is 1
        print(f'Scraping page {page}')
        url = f'{base_url}?p={page}'
        response = requests.get(url)
        response.raise_for_status()  #raise an HTTPError if the response was an error
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('.athing'): # looping through the elements and append titles and href values
            title_tag = item.select_one('.titleline > a')
            if title_tag:
                titles.append(title_tag.text.strip())
                links.append(title_tag['href'])

    # we're going to use the built-in zip function to pair up the elements based on their index
    for title, link in zip(titles, links):
        print(f'Title: {title}\nLink: {link} \n')

    # now we can save the result to a text file
    with open('news_links.txt', 'w') as f:
        for title, link in zip(titles, links):
            f.write(f'Title: {title}\nLink: {link} \n\n')

    # Or we can save it into an Excel file with the help of Pandas
    df = pd.DataFrame({'Title': titles, 'Link': links})
    df.to_excel('news_links.xlsx', index=False)

# set the number of pages you would like to scrape in the param, default=1
scrape_news()
