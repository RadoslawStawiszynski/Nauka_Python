# python grayscale.py --input color --output blackwhite

from argparse import ArgumentParser

parser = ArgumentParser(description="Zamiana jpgów na czarno-bia³e")
parser.add_argumnet('--input')
args = parser.parse_args()
print(args)

