# Importing libraries.
import pickle
import PTN
import episodegrab
import checklatest


# Take info entered parse it and add current episode and choses quality to database
def store_show(info):

    shows = []
    show = PTN.parse(info)
    shows.append(show)


    #Checking for shows in memory, if no shows found add new list with one new show.
    try:
        file = open('myshows.txt', 'rb')
    except IOError:
        file = open('myshows.txt', 'wb')

    try:
        storedshows = pickle.load(file)
    except EOFError:
        file = open('myshows.txt', 'wb')
        pickle.dump(shows,file)
        storedshows = shows

    # Checking if show exists in memory, if not add.
    if not any(value['title']== show['title'] for value in storedshows) :
        file = open('myshows.txt', 'rb')
        shows = pickle.load(file)
        shows.append(show)
        file = open('myshows.txt', 'wb')
        pickle.dump(shows, file)



    # Return the list of shows.
    file=open('myshows.txt','rb')
    return pickle.load(file)
    file.close()

# Remove a show from the myshows.txt
def remove_show(title):
    try:
        file = open('myshows.txt', 'rb')
        shows=pickle.load(file)
        updatedshows=[]
        for show in shows:
            if show['title']!=title:
                updatedshows.append(show)
        file=open('myshows.txt','wb')
        pickle.dump(updatedshows,file)
        file.close()
        print 'Show removed!'


   # Searching the next episode for all episodes in myshows.txt.
def grab_latest():
    file=open('myshows.txt','rb')
    shows=pickle.load(file)

    # Checking what data is available and using it to search for episode with desired (if desired) quality or resolution.
    for show in shows:
        medianame=show['title']
        print medianame
        if show.has_key('season') and show.has_key('episode'):
            if show['season']<10:
                medianame+= ' S'+'0'+show['season']
            if show['season']>9:
                medianame=+' S'+ show['season']
            if show['episode']<10:
                medianame+= 'E'+'0'+show['episode']
            if show['episode']>9:
                medianame+='E'+ show['episode']

        # If no episode is entered grab latest released episodes.
        else:
            medianame=checklatest.checklatest(show['title'])

        if show.has_key('quality'):
            medianame+=' ' + show['quality']
        if show.has_key('resolution'):
            medianame+=' '+ show['resolution']
        episodegrab.grabepis

