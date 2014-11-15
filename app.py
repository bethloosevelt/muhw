__author__ = 'dalewesa'

import flask
from flask import Flask
from flask import render_template
import json
from werkzeug.serving import run_simple
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/musicplayer")
def sendembed():
    embedHTML = {'embed': '<iframe width="100%" height="80%" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/users/12006695&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false"></iframe>'}
    return flask.jsonify(embedHTML)

if __name__ == "__main__":
    #run_simple("homestylebeatz.com", 80, app)
    app.run(debug=True)
