from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Acer/Downloads/chromedriver_win32/chromedriver.exe")
    elif browser=="firefox":
        driver=webdriver.Firefox(executable_path="C:/Users/Acer/Downloads/geckodriver-v0.27.0-win64/geckodriver.exe")
    else:
        driver=webdriver.Edge(executable_path="C:/Users/Acer/Downloads/edgedriver_arm64/msedgedriver.exe")
    return driver




def add_option(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

