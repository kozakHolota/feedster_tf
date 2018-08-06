from abc import abstractmethod

from rest.request import Request


class AppAbstract(object):

    def __init__(self, host, endpoint):
        self.endpoint = endpoint
        self.request = Request(host)

    @abstractmethod
    def perform(self, log_request=True):
        pass