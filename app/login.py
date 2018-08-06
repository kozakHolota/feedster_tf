import allure
from app.app_abstract import AppAbstract
from data_models.login_data_model import LoginDataModel


class Login(AppAbstract):

    def __init__(self, host, username, password):
        super().__init__(host, "/v1/auth/login/")
        self.password = password
        self.username = username

    @allure.step("Logging into Feedster API")
    def perform(self, log_request=True):
        return LoginDataModel(
            self.request.post_endpoint(self.endpoint,
                                          data="username={}&password={}".format(self.username,
                                                                                              self.password,
                                                                                log_request=log_request)
                                       )
        )