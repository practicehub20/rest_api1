import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


def json_to_dict(json_data):
    stream = io.BytesIO(json_data)
    dict_data = JSONParser().parse(stream)
    return dict_data

def dict_to_json(serialize_obj):
    json_data = JSONRenderer().render(serialize_obj)
    return json_data

