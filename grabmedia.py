import episodegrab
import checklatest
import storemedia
import argparse
parser = argparse.ArgumentParser()
def Main():

    parser.add_argument("-e","--episode", help="Search for an episode on EZT. Enter show name and use format.'\
     'S##E##, quality and/or resolution also optional. ",action="store_true")

    parser.add_argument("-l", "--latest", help="Get the latest episode available of a show.'\
     'you can also specify resolution and/or quality. ", action="store_true")

    parser.add_argument("-a", "--addshow", help="Add a show to the database.'\
     'you can also specify resolution and/or quality. ", action="store_true")

    parser.add_argument("-r", "--removeshow", help="Remove show from database", action="store_true")

    parser.add_argument("-u", "--updateshows", help="Get the latest episodes available of all shows in database. ", action="store_true")



    parser.add_argument("media", help="Media wanted ", type=str)

    args = parser.parse_args()

    if args.episode:
        episodegrab.grabepisode(args.media)

    if args.latest:
        episodegrab.grabepisode(checklatest.checklatest(args.media))

    if args.addshow:
        storemedia.store_show(args.media)

    if args.removeshow:
        storemedia.remove_show(args.media)

    if args.updateshows:
        storemedia.grab_latest


if __name__ == '__main__':
    Main()