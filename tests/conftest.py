import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #renaming

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver=webdriver.Chrome(executable_path="C:\\Users\\venka\\PycharmProjects\\PythonSelFramework\\executablefiles\\chromedriver_83.exe")
    elif browser_name=="firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\venka\\PycharmProjects\\PythonSelFramework\\executablefiles\\geckodriver.exe")
    elif browser_name=="IE":
        driver = webdriver.IE(executable_path="C:\\Users\\venka\\PycharmProjects\\PythonSelFramework\\executablefiles\\IEDriverServer.exe")

    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()