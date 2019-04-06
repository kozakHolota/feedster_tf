from setuptools import setup
# Veni! Vidi! Vichi
setup(
name = "Feedster REST API Testing Framework",
version = "1.0.0-beta",
author = "Pavlo Mryhlotskyi",
author_email = "kozak.holota@gmail.com",
maintainer = "Sich Mobile",
install_requires=["requests", "pytest", "allure-pytest"]
)