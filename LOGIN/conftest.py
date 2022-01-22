from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=["chrome"], scope='class')
def init__driver(request):
    if request.param=="chrome":
       web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param=="firefox":
       web_driver = webdriver.Firefox(executeable_path = GeckoDriverManager().install())
    request.cls.driver=web_driver
    web_driver.implicitly_wait(15)

    """ TEARDOWN"""
    yield
    web_driver.quit() 