from requests import Response

from data_models.abstrract_data_model import AbstractDataModel


class LogoutDataModel(AbstractDataModel):
    def __init__(self, resp: Response):
        super().__init__(resp)

    def __eq__(self, other):
        return self.status_code == other.status_code