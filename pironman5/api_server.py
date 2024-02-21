from flask import Flask, request
import threading
import json
from werkzeug.serving import make_server
from utils import log

host = '0.0.0.0'
port = 34002
path_prefix = '/api/v1'
app = Flask(__name__)
thread = None

config = {
    'unit': "C",
    'rgb_enable': True,
    'rgb_style': "breath",
    'rgb_color': "0a1aff",
    'rgb_num': 4,
    'rgb_speed': 50,
    'rgb_freq': 1000,
}


def on_change(config):
    print(f'config: {config}')

@app.route('/')
def root():
    return 'Hello, Root!'

@app.route(path_prefix+'/hello')
def hello():
    return 'Hello, World!'

@app.route(path_prefix + 'get_config', methods=['GET'])
def get_config():
    return config

@app.route(path_prefix + 'set_config', methods=['POST'])
def set_config():
    config_string = request.form['config']
    config = json.loads(config_string)
    log(f'set_config: {config}')

class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def run():
    global server, app
    server = ServerThread(app)
    server.start()
    log(f'API server started at {host}:{port}')

def stop():
    global server
    server.shutdown()
    log('API server stopped')