# Importing libraries.
from bs4 import BeautifulSoup
import requests
import re
import PTN


# Scrape EZTV.
def search_eztv(name):

    # Getting search engine.
    resp = requests.get("https://eztv.ag/search/" + name)
    soup = BeautifulSoup(resp.content, "lxml", )

    # Finding show magnets.
    columns=[] # Finding torrent site table format attributes.
    torrents=[] # Available torrent results.

    # Getting columns.
    for column in soup.find_all('td',{'class': 'forum_thread_header'}) :
        if column.text!='':
            columns.append(column.text)

    # Getting torrent info.
    for record in soup.find_all('tr',{'class': 'forum_header_border'}) :
      i=0
      values = {}           # Attribute values for specific result.
      torratr = []          # General usable attributes for display by table order.

    # Getting values.
      for data in record.findAll('td'):

        if data.text !='' and not data.text.isspace():
            torratr.append(columns[i])
            values.update({columns[i]:data.text.strip('\n')})
        i+=1
      torrents.append(values)

    # Getting magnets and ignorig double magnet links.

    links=[]
    magnets=soup.find_all('a', {'class': 'magnet'})
    if len(magnets)<=len(torrents):
        i = 0
        for link in soup.find_all('a', {'class': 'magnet'}):
            torrents[i].update({'Magnet': link['href']})
            i += 1
    else:
        i = 0
        t = 1
        for link in soup.find_all('a', {'class': 'magnet'}):

            links.append(link.get('title'))

            if  len(links)==1 or links[i]!=links[i-1]:
                torrents[t].update({'Magnet': link['href']})
                t+=1
            i+=1

    # Getting downloads
    i=0
    for link in soup.find_all('a', {'class': 'download_1'}):
        torrents[i].update({'Torrent': link['href']})
        i+=1


    # Return usable values.

    return (torrents)















