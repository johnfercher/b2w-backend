from functools import wraps
from flask import Response


def has_valid_data_in_response(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = f(*args, **kwargs)

        if data is None:
            return Response(status=404)

        if type(data) is list:

            jsons = [element.to_json() for element in data]
            json = ','.join(jsons)
            json = "[{0}]".format(json)
            return Response(json, status=200, mimetype='application/json')
        else:
            return Response(data.to_json(), status=200, mimetype='application/json')

    return decorated_function
