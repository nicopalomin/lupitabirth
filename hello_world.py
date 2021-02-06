import os

import cherrypy
from jinja2 import Environment, FileSystemLoader

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
env=Environment(loader=FileSystemLoader(CUR_DIR),
trim_blocks=True)

class Root(object):
    @cherrypy.expose
    def index(self):
        return env.get_template('html/index.html').render()

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')
