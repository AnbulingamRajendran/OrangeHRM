# For cross browser options
# In conftest.py
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Browser not supported")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


'''| Browser | Command                    |
| ------- | -------------------------- |
| Chrome  | `pytest --browser=chrome`  |
| Edge    | `pytest --browser=edge`    |
| Firefox | `pytest --browser=firefox` |
'''


#For parallel execution

# -> pip install pytest-xdist
'''| Purpose                        | Command                 |
| ------------------------------ | ----------------------- |
| Run on 2 threads               | `pytest -n 2`           |
| Run on all available CPU cores | `pytest -n auto`        |
| Run parallel + marker          | `pytest -n 3 -m sanity` |
'''

# Verbose and reporting

'''| Purpose                          | Command        |
| -------------------------------- | -------------- |
| Show detailed logs               | `pytest -v`    |
| Show print statements in console | `pytest -s`    |
| Combine both                     | `pytest -v -s` |
| Stop after first failure         | `pytest -x`    |
| Run failed tests only (rerun)    | `pytest --lf`  |
| Show last failed + all new tests | `pytest --ff`  |
'''

# HTML - Report

# -> pytest -v -s --html=Reports/report.html
# ->pytest -v -s --html=Reports/report_$(date +%d-%m-%Y_%H-%M-%S).html

''''| Scenario                                | Example Command                                                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Run only sanity on Chrome               | `pytest -m sanity --browser=chrome -v -s`                                                                        |
| Run regression on Firefox with report   | `pytest -m regression --browser=firefox -v --html=Reports/regression.html`                                       |
| Run parallel sanity tests on 3 browsers | `pytest -n 3 -m sanity --browser=edge -v`                                                                        |
| Run specific test with logs and report  | `pytest TestCases/test_category.py::TestCategorySanity::test_category_sanity -v -s --html=Reports/category.html` |
'''

#other flags

'''| Flag                 | Description                |
| -------------------- | -------------------------- |
| `--maxfail=2`        | Stop after 2 test failures |
| `--disable-warnings` | Hide warnings in output    |
| `--tb=short`         | Short traceback format     |
| `--tb=none`          | Hide traceback completely  |
| `--durations=5`      | Show 5 slowest tests       |
'''
