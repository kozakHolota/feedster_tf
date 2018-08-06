import allure
import requests
from requests import Response


class Request(object):
    def __init__(self, host):
        self.host = host

    @property
    def content_type(self):
        return "application/json"

    @property
    def con_method(self):
        return 'https'

    @property
    def get(self):
        return requests.get

    @property
    def post(self):
        return requests.post

    @property
    def put(self):
        return requests.put

    @property
    def update(self):
        return requests.put

    @property
    def head(self):
        return requests.head

    @property
    def options(self):
        return self.options

    @property
    def delete(self):
        return requests.delete

    def log_response(self, response: Response):
        status_code = str(response.status_code)
        allure.attach(status_code, "Status Code")
        allure.attach(response.content, "Response content")
        allure.attach(str(response.headers.items()), "Headers")

    def get_url(self, end_point):
        return '{}://{}{}'.format(self.con_method, self.host, end_point)

    def get_endpoint(self, end_point: str, additional_headers=None):
        if additional_headers is None:
            additional_headers = {}

        resp = self.get(self.get_url(end_point), headers=dict(**{"Content-Type": "application/x-www-form-urlencoded"}, **additional_headers))

        self.log_response(resp)

        return resp

    def post_endpoint(self, end_point: str, additional_headers=None, json=None, data=None):
        if additional_headers is None:
            additional_headers = {}

        resp = self.post(self.get_url(end_point), headers=dict(**{"Content-Type": "application/x-www-form-urlencoded"}, **additional_headers), json=json, data=data)

        self.log_response(resp)

        return resp

    def delete_endpoint(self, end_point: str, additional_headers=None):
        resp = self.delete(self.get_url(end_point), headers=dict(**{"Content-Type": "application/x-www-form-urlencoded"}, **additional_headers))

        self.log_response(resp)

        return resp