import flask
import tasks

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    to_say = flask.request.args.get('to_say')
    tasks.say(to_say)
    return flask.jsonify({'status': 'ok'})
