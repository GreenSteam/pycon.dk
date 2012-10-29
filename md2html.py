#!/usr/bin/env python
import sys

from markdown import markdown


template = open('TEMPLATE.html').read().decode('utf8')

for file in sys.argv[1:]:
    new_file = file.rstrip('.md') + '.html'
    print '%s -> %s' % (file, new_file)
    html = markdown(open(file).read().decode('utf8'))
    html = template.replace('{{body}}', html)
    open(new_file, 'w').write(html.encode('utf8'))
