import flask
import tasks

app = flask.Flask(__name__)


@app.route("/say", methods=['POST'])
def say():
    request_data = flask.request.get_json()
    to_say = request_data['to_say']
    if not to_say:
        flask.abort(400)
    tasks.say(to_say)
    return ('', 204)
