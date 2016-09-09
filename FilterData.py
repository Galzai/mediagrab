# Importing libraries
import PTN
import Scraper


# Returns true if search parameters are met.
def analyze(input, name, season='',episode='', resolution='', quality=''):

    matches = []
    data=[]

# If for some reason there is not magnet or torrent link but result is shown remove it.
    for torrent in input:
        if torrent.has_key('Magnet') or torrent.has_key('Torrent'):
            data.append(torrent)

    for torrent in data:
        # Has key is used to check if PTN can extract certain info from filename for filtering results.
        # (PTN creates a dict with found parameters as keys).

        key1 = PTN.parse(torrent['Episode Name']).has_key('season')
        key2 = PTN.parse(torrent['Episode Name']).has_key('episode')
        key3 =  PTN.parse(torrent['Episode Name']).has_key('resolution')
        key4 = PTN.parse(torrent['Episode Name']).has_key('quality')

# f-i checks if value for parameter is entered (the only that can't be blank is show title).
        f = season != ''
        g = episode != ''
        h = resolution != ''
        i = quality != ''
        a = PTN.parse(torrent['Episode Name'])['title'].lower() != name.lower()

# Checks if a value for parameter is entered and matches PTN result (if data is available).
        b=True
        c=True
        d=True
        e=True
        if key1:
            b = PTN.parse(torrent['Episode Name'])['season'] != season

        if key2:
            c = PTN.parse(torrent['Episode Name'])['episode'] != episode

        if key3:
            d = PTN.parse(torrent['Episode Name'])['resolution'].lower() != resolution.lower()

        if key4:
            e = PTN.parse(torrent['Episode Name'])['quality'].lower() != quality.lower()

        n1 =(not key1) and f
        n2 = (not key2) and g
        n3 = (not key3) and h
        n4 = (not key4)  and i

# If parameter exists and required add torrent to matches.
        if not (a or (b and f) or (c and g) or (d and h) or (e and i)):
            matches.append(torrent)

# If parameter required but does not exist remove the value from matches (this required because of the way PTN works).
        if (n1 or n2 or n3 or n4) and matches !=[]:
            matches.remove(torrent)

    return matches



