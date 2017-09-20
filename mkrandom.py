#!/usr/bin/python

import math
import random


def gaussian(low, high, mu, sigma):
    '''
    Generate a number (float) between `low` and `high` that
    fits a gaussian distribution of `mu` and `sigma`.
    '''
    while True:
        x = low + (high-low) * random.random()
        try:
            p = 1/(sigma*math.sqrt(2*math.pi)) / math.e**(((x-mu)/sigma)**2)
        except OverflowError:
            continue
        if random.random() < p:
            return x


def polygon(settings):
    return ''

def create(filename, polygons, settings):
    output = open(filename, 'w')
    output.write(
        '<svg width="{0}mm" height="{1}mm" viewBox="0 0 {0} {1}"\n'
        'xmlns="http://www.w3.org/2000/svg">\n'
        '<rect x="0" y="0" width="{0}" height="{1}"\n'
        'fill="{2}"/>\n'.format(
            settings['width'],
            settings['height'],
            settings['background'],
        )
    )
    for _ in range(polygons):
        output.write(polygon(settings))
    output.write('</svg>\n')

def main():
    create('test.svg', 20, {
        'width': 297,
        'height': 420,
        'background': '#ffffff',
    })


if __name__ == '__main__':
    main()

