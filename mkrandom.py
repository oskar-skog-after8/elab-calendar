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
    x = random.random() * settings['width']
    y = random.random() * settings['height']
    origo = x, y

    max_radius = math.sqrt(settings['width']**2 + settings['height']**2)
    shape = settings['shape']
    points = []
    angle = 0
    while angle < 2*math.pi:
        angle += gaussian(0, 2*math.pi, *shape['angular-velocity'])
        r = gaussian(0, max_radius, *shape['radius'])
        x = origo[0] + r*math.cos(angle)
        y = origo[1] - r*math.sin(angle)
        points.append('{},{}'.format(x, y))
    
    color = settings['color']
    color_s = "hsl({}, {}%, {}%)".format(
        gaussian(0, 360, *color['hue']),
        gaussian(0, 100, *color['saturation']),
        gaussian(0, 100, *color['value'])
    )

    svg = '    <polygon points="{}" fill="{}" fill-opacity="{}"/>\n'.format(
        ' '.join(points), color_s, gaussian(0, 100, *color['opacity'])/100)
    
    if settings['contrast-zone'](origo):
        opacity = settings['contrast-overlay-opacity'][0]
    elif any(map(settings['contrast-zone'], points)):
        opacity = settings['contrast-overlay-opacity'][1]
    else:
        return svg
    svg += '      <polygon points="{}" fill="{}" fill-opacity="{}"/>\n'.format(
        ' '.join(points), settings['background'], opacity/100.0)
    return svg

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
    create('test.svg', 1000, {
        'width': 297,
        'height': 420,
        'background': '#ffffff',
        'color': {
            'hue': (45, 50),
            'saturation': (80, 15),
            'value': (33, 25),
            'opacity': (90, 10)
        },
        'shape': {
            'radius': (50, 60),
            'angular-velocity': (.2, 1),
        },
        'contrast-overlay-opacity': (60, 50),
        'contrast-zone': lambda point: 20 < point[0] < 277 and 250 < point[1] < 400,
    })


if __name__ == '__main__':
    main()

