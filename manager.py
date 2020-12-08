#!/usr/bin/env python
from flask_script import Manager, Server
from app import create_app
import os

port = os.getenv("PORT") if os.getenv("PORT") else 5000

app = create_app() ## <-- factory method to switch between configurations
app.secret_key = "1234567890"

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=port))

@manager.shell
def make_shell_context():
    return dict(app=app)
 
if __name__ == "__main__":
    manager.run()