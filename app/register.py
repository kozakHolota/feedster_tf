import allure
from app.app_abstract import AppAbstract
from data_models.registration_data_model import RegistrationDataModel


class Register(AppAbstract):
    def __init__(self, host, username, password1, password2):
        super().__init__(host, "/v1/auth/registration/")
        self.password2 = password2
        self.password1 = password1
        self.username = username

    @allure.step("Registering new user into ")
    def perform(self):
        return \
            RegistrationDataModel(
                self.request.post_endpoint(
                    self.endpoint,
                    data="username={}&password1={}&password2={}".format(
                        self.username,
                        self.password1,
                        self.password2
                    )
                )
            )
