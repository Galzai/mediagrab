import episodegrab
import argparse
parser = argparse.ArgumentParser()
def Main():
    parser.add_argument("-e","--episode", help="Search for an episode on EZT. Enter show name and use format. S##E##, quality and/or resolution also optional. ",action="store_true")

    parser.add_argument("episode", help="Episode wanted ", type=str)
    args = parser.parse_args()

    if args.episode:
        episodegrab.grabepisode(args.episode)

if __name__ == '__main__':
    Main()