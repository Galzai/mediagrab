# Importing libraries.

from bs4 import BeautifulSoup
import requests
import re
import PTN


def checklatest(show):

    title=PTN.parse(show)['title']
    # Formatting the name for TV.com -name must be accurate ("ie daredevil= marvels daredevil).
    output=''
    fshow=title.replace(' ','-')

    # Getting search engine (TV.com).
    resp = requests.get("http://www.tv.com/shows/" + fshow)
    soup = BeautifulSoup(resp.content, "lxml", )

    result= soup.find('p',{'class': 'highlight_season'}).text.strip('\n')
    data=[int(s) for s in result.split() if s.isdigit()]

    # Formatting for normal S##E##
    if data[0]<10:
        output+='S'+'0'+str(data[0])
    else:
        output+='S'+str(data[0])

    if data[1]<10:
        output+='E'+'0'+str(data[1])
    else:
        output+='E'+str(data[1])

    return show+' ' +output


