# python grayscale.py --input color --output blackwhite

from argparse import ArgumentParser

parser = ArgumentParser(description="Zamiana jpg�w na czarno-bia�e")
parser.add_argumnet('--input')
args = parser.parse_args()
print(args)

