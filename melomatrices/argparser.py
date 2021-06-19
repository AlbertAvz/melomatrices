import argparse

parser = argparse.ArgumentParser(prog='melomatrices')

parser.add_argument('Path',
                    type=str,
                    help='the path to MIDI')

args = parser.parse_args()

path = args.Path
