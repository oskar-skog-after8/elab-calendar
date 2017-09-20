#!/usr/bin/python

def polygon(width, height):
    return ''

def create(filename, polygons, width=297, height=420, background='#ffffff'):
    output = open(filename, 'w')
    output.write(
        '<svg width="{0}mm" height="{1}mm" viewBox="0 0 {0} {1}"\n'
        'xmlns="http://www.w3.org/2000/svg">\n'
        '<rect x="0" y="0" width="{0}" height="{1}"\n'
        'fill="{2}"/>\n'.format(width, height, background)
    )
    for _ in range(polygons):
        output.write(polygon(width, height))
    output.write('</svg>\n')

def main():
    create('test.svg', 20)


if __name__ == '__main__':
    main()

