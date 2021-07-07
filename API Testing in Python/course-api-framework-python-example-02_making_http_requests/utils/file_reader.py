import json

from pathlib import Path


PATH = Path.cmd().joinpath('..','tests','data')

def read_file(file_name):
    path = get_file_with_json_extesion(file_name)

    with path.open(mode='r') as f:
        return json.load(f)

def get_file_with_json_extesion(file_name):
    if  file_name.endswith('.json'):
        path = PATH.joinpath(file_name)
    else:
        path = PATH.joinpath(f'{file_name}.json')
    return path