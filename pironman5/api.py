from flask import Flask
import threading

path_prefix = '/api/v1'
app = Flask(__name__)
thread = None

def onChage(config):
    print(f'config: {config}')

@app.route(path_prefix+'/hello')
def hello():
    return 'Hello, World!'

def run():
    app.run()

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