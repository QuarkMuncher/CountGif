from flask import Flask, send_file
import main

app = Flask(__name__)


@app.route("/<name>/<countdown>")
def hello_world(name, countdown):
    filename = "{}.gif".format(name)
    mainObject = main.Main()
    mainObject.main(name=filename, countdown=countdown)
    return send_file(filename, mimetype="image/gif")
