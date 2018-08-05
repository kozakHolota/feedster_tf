import allure

from app.register import Register


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify possibility to register new user")
@allure.feature("Register")
def test_registration(host, username, password1, password2, expected_response):
    assert Register(host, username, password1,
                    password2).perform() == expected_response, "Actual response to registration request does not equal to expected one"
