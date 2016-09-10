# Import libraries
import  FilterData
import Scraper
import os
import PTN


def grabepisode(show):

    data= PTN.parse(show)

    # Making sure a show name was entered
    if not data.has_key('title'):
        print 'No show entered'

    # If a name was entered output results and give options to download.
    else:

        season=''
        episode=''
        resolution=''
        quality=''

        name=data['title']

        if data.has_key('season'):
            season=data['season']

        if data.has_key('episode'):
            episode=data['episode']

        if data.has_key('resolution'):
            resolution=data['resolution']

        if data.has_key('quality'):
            quality=data['quality']


        a=''
        b=''

    # Filter resuluts to remove non matching results (some results from torrent sites are suitable).
        results=Scraper.search_eztv(show)
        filtered=FilterData.analyze(results,name,season,episode,resolution,quality)

    # Output filtered data found and allow for selection of magnet or torrent, if non found alert user.
        i=1
        for torrent in filtered:
            print '['+ str(i) +']'

            for key in torrent:

                if key!='Magnet' and key!='Torrent':
                    print key+': ' + torrent[key]

                if key=='Magnet':
                    a='   Magnet available!  '

                if key == 'Torrent':
                    b = '   Torrent available!   '
            print a+b
            print''
            i+=1
            a=''
            b=''
        if filtered!=[]:
            print 'Choose wanted torrent:'
            torrnum=raw_input()

            print 'Choose enter Magnet for magnet or Torrent for torrent'
            selected=raw_input()
            os.startfile(filtered[int(torrnum)-1][selected])
        else:
            print 'No media found!'





