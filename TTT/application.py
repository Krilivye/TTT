import werkzeug
import json
from TTT.exemples import super_additionneur

def application(environ, start_response):
    _request = werkzeug.Request(environ)
    _data = json.loads(_request.get_data().decode("utf-8"))

    to_json = { "result": super_additionneur(_data["param1"], _data["param2"]) }

    return werkzeug.Response(
        json.dumps(to_json),
        mimetype='application/json') \
            (environ, start_response)
