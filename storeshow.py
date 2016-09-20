# Importing libraries.
import pickle
import PTN


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




