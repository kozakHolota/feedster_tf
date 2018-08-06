from app.register import Register
from data_models.login_data_model import LoginDataModel
from utils.generator import generate_string


def pytest_generate_tests(metafunc):
    feedster_host = r"api.feedster.me"
    default_username = generate_string(8)
    incorrect_username = generate_string(8)
    empty_username = ''
    pass8 = generate_string(8)
    incorrect_pass = generate_string(8)
    empty_pass = ''
    # resp = Register(feedster_host, default_username, pass8,
    #                 pass8).perform()
    # status = int(resp.status_code)
    #
    # while status != 201:
    #     default_username = generate_string(8)
    #     pass8 = generate_string(8)
    #     resp = Register(feedster_host, default_username, pass8,
    #                       pass8).perform()
    #     status = int(resp.status_code)

    metafunc.parametrize("host, username, password, expected_response",
                         (
                             (feedster_host, default_username, pass8, LoginDataModel({"key": "0uguyguyg7786785"}, response_code=200)),
                          (feedster_host, default_username, incorrect_pass, LoginDataModel({"non_field_errors":["Unable to log in with provided credentials."]}, response_code=400)),
                             (feedster_host, incorrect_username, pass8, LoginDataModel({"non_field_errors":["Unable to log in with provided credentials."]}, response_code=400)),
                              (feedster_host, empty_username, pass8, LoginDataModel({"username":["This field may not be blank."]}, response_code=400)),
                             (feedster_host, default_username, empty_pass,
                              LoginDataModel({"password": ["This field may not be blank."]}, response_code=400))
                          )
                         )

