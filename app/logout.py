import allure
from app.app_abstract import AppAbstract
from data_models.logout_data_model import LogoutDataModel


class Logout(AppAbstract):
    def __init__(self, host):
        super().__init__(host, "/v1/auth/logout/")

    @allure.step("Logout from the system")
    def perform(self, log_request=True):
        return LogoutDataModel(self.request.post_endpoint(self.endpoint, log_request=log_request))