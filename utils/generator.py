from base64 import b64encode
from os import urandom


def generate_string(symbols_num: int):
    return b64encode(urandom(symbols_num)).decode('utf-8').replace(r'=', '-').replace(r'/', r'-').replace(r'\\', r'_').replace(r'+', r'_')[:symbols_num]