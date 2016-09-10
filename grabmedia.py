import episodegrab
import checklatest
import argparse
parser = argparse.ArgumentParser()
def Main():
    parser.add_argument("-e","--episode", help="Search for an episode on EZT. Enter show name and use format.'\
     'S##E##, quality and/or resolution also optional. ",action="store_true")



    parser.add_argument("-l", "--latest", help="Get the latest episode available of a show.'\
     'you can also specify resolution and/or quality. ", action="store_true")

    parser.add_argument("media", help="Media wanted ", type=str)

    args = parser.parse_args()

    if args.episode:
        episodegrab.grabepisode(args.media)

    if args.latest:
        episodegrab.grabepisode(checklatest.checklatest(args.media))


if __name__ == '__main__':
    Main()