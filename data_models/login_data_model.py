from requests import Response

from data_models.abstrract_data_model import AbstractDataModel


class LoginDataModel(AbstractDataModel):
    def __init__(self, resp, response_code=None):
        super().__init__(resp, response_code=response_code)

    def __eq__(self, other):
        print("Actual status code: {}. Expected {}".format(self.status_code, other.status_code))
        print("Actual fields: {}\nExpected: {}".format(self.__dict__, other.__dict__))
        return self.status_code == other.status_code and (self.__dict__.keys() == other.__dict__.keys())