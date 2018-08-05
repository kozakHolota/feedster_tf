from requests import Response

from data_models.registration_data_model import RegistrationDataModel
from utils.generator import generate_string


def pytest_generate_tests(metafunc):
    feedster_host = r"api.feedster.me"
    default_username = generate_string(8)
    pass8 = generate_string(8)
    another_pass8 = generate_string(8)
    pass20 = generate_string(20)
    pass5 = generate_string(5)
    pass0 = ''

    empty_usr = ''

    metafunc.parametrize("host, username, password1, password2, expected_response", (
        (feedster_host, default_username, pass8, pass8, RegistrationDataModel({"key": "0knndieheroih"} ,response_code=201)),
        (feedster_host, generate_string(5), pass20, pass20, RegistrationDataModel({"key": "0knndieheroih"} ,response_code=201)),
        (feedster_host, generate_string(5), pass8, another_pass8, RegistrationDataModel({"non_field_errors": ["The two password fields didn't match."]} ,response_code=400)),
        (feedster_host, generate_string(5), pass5, pass5, RegistrationDataModel({"password1": ["This password is too short. It must contain at least 8 characters."]} ,response_code=400)),
        (feedster_host, generate_string(5), pass0, pass0,
         RegistrationDataModel({"password1": ["This field may not be blank."],"password2": ["This field may not be blank."]},
                               response_code=400)),
        (feedster_host, empty_usr, pass8, pass8,
         RegistrationDataModel(
             {"username": ["This field may not be blank."]},
             response_code=400)),
        (feedster_host, default_username, pass20, pass20, RegistrationDataModel({"username":["A user with that username already exists."]}, response_code=400))
    )
                         )

