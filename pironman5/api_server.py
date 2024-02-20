from flask import Flask, request
import threading
import json
from werkzeug.serving import make_server
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

# def _run():
#     app.run(host='0.0.0.0', port=34002, debug=False, use_reloader=False)

# def run():
#     global thread
#     thread = threading.Thread(target=_run)
#     thread.start()

# def stop():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()
#     thread.join()

class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server('0.0.0.0', 34002, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        log('starting server')
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

def run():
    global server
    server = ServerThread(app)
    server.start()
    log('server started')

def stop():
    global server
    server.shutdown()