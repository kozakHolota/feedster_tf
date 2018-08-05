import allure

from app.login import Login


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify possibility to register new user")
@allure.feature("Login")
def test_login(host, username, password, expected_response):
    assert Login(host, username, password).perform() == expected_response, "Login process result is not the same as expected"