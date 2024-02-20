from flask import Flask, request
from werkzeug.serving import make_server
import threading
import json
from utils import log

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


def run():
    app.run(host='0.0.0.0', port=34002, debug=False, use_reloader=False)

def run_in_thread():
    global thread
    thread = threading.Thread(target=run)
    thread.start()

class APIServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', 34002, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('starting server')
        self.srv.serve_forever()

    def stop(self):
        self.srv.shutdown()

    def set_config(self, data):
        global config
        config = data

    def set_on_change(self, func):
        global on_change
        on_change = func
