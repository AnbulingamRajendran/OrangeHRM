import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report for dev"


def pytest_configure(config):
    config.stash[metadata_key]["Project name"] = "Orange HRM"
    config.stash[metadata_key]["Tester"] = "Anbulingam"
    if "JAVA_HOME" in config.stash[metadata_key]:
        del config.stash[metadata_key]["JAVA_HOME"]
    if "Packages" in config.stash[metadata_key]:
        del config.stash[metadata_key]["Packages"]


def pytest_collection_modifyitems(items):
    order = ['test_title_check', 'test_login_check', 'test_addEmp', 'test_SearchEmp', 'test_deleteEmp', 'test_login_DDT']
    items.sort(key=lambda item: order.index(item.name) if item.name in order else len(order))




