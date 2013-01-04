import os
import sys

syspaths = []

for directory in (os.path.abspath('eggs'), os.path.abspath('src')):
    for file in os.listdir(directory):
        syspaths.append(os.path.join(directory, file))

sys.path[0:0] = syspaths

from pyramid.paster import get_app
from paste.script.util.logging_config import fileConfig

here = os.path.dirname(os.path.abspath(__file__))
conf = os.path.join(here, 'etc', 'production.ini')
fileConfig(conf)

application = get_app(conf, 'main')
