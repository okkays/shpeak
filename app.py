import flask
import tasks

app = flask.Flask(__name__)


@app.route("/say", methods=['POST', 'OPTIONS'])
def say():
    response = flask.Response('')
    response.status = 204
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Headers', '*')

    if flask.request.method == 'OPTIONS':
        return response

    request_data = flask.request.get_json()
    to_say = request_data['to_say']
    if not to_say:
        flask.abort(400)
    tasks.say(to_say)
    return response
