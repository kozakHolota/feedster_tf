import json
from abc import abstractmethod

from requests import Response


class AbstractDataModel(object):
    def __init__(self, data, response_code=None):
        self.status_code = None
        if isinstance(data, Response):
            self.status_code = int(data.status_code)
            content: dict = json.loads(data.content)
            for entry in content:
                self.__dict__[entry] = content[entry]
        elif isinstance(data, dict):
            if not response_code:
                self.status_code = 200
            else:
                self.status_code = response_code

            for entry in data:
                self.__dict__[entry] = data[entry]
        else:
            raise ValueError("Data should be Response or dict, not {}".format(type(data)))


    @abstractmethod
    def __eq__(self, other):
        pass

    def __repr__(self):
        return str(self.__dict__)