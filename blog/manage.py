import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from blog import (app, config)

manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=config.debugger, use_reloader=config.reloader, host='0.0.0.0', port=8000))

if __name__ == '__main__':
    manager.run()