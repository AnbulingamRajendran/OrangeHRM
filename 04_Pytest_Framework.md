# 04 - Pytest Framework

## Project structure
```
tests/
  pages/         # POM classes
  tests/         # test_*.py files
conftest.py      # fixtures
```
## Fixtures & Scopes
```python
import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()
```

## Markers, Parametrize
```python
@pytest.mark.sanity
def test_login(driver): pass

@pytest.mark.parametrize("username,password", [("u1","p1"),("u2","p2")])
def test_creds(driver, username, password): pass
```

## Setup/teardown
Use fixtures for setup/teardown rather than unittest classes.

## CLI options
```
pytest -m sanity
pytest -k login
pytest --html=report.html
```

## Parallel execution
Use `pytest-xdist`:
```
pytest -n 4
```