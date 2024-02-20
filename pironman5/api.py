from flask import Flask
import threading

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


def onChage(config):
    print(f'config: {config}')

@app.route(path_prefix+'/hello')
def hello():
    return 'Hello, World!'

@app.route(path_prefix + 'get_config', methods=['GET'])
def get_config():
    return config

def run():
    app.run(host='0.0.0.0', port=34002, debug=False, use_reloader=False)

def run_in_thread():
    global thread
    thread = threading.Thread(target=run)
    thread.start()

def stop():
    global thread
    if thread:
        thread.join()
        thread = None

if __name__ == '__main__':
    try:
        run_in_thread()
    except KeyboardInterrupt:
        pass
    finally:
        stop()