import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "headless":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_option)
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_metadata(metadata):
    metadata["Project Name"] = "orange_hrm"
    metadata["Module Name"] = "Login"
    metadata["Tester Name"] = "teamlion"
    metadata["URL"] = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.fixture(params=[("Admin", "admin123", "pass"),
                        ("Admin1", "admin123", "fail"),
                        ("Admin", "admin1231", "fail"),
                        ("Admin1", "admin1231", "fail")])
def get_data_for_login(request):
    return request.param
