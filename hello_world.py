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
    cherrypy.config.update({'engine.autoreload.on':False})
    cherrypy.config.update({
    'log.screen':True,
    'tools.sessions.on': True,
    'checker.on':False,
    'server.socket_host':'192.168.0.167',
    'tools.staticdir.root': '/home/pi/pythonprogs',
    'tools.staticdir.on': True,
    'tools.staticdir.dir':'static'})
