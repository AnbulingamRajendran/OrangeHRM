# 05 - Page Object Model (POM)

## Folder structure
```
pages/
  base_page.py
  home_page.py
tests/
  test_home.py
```

## BasePage example
```python
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator): return self.driver.find_element(by, locator)
    def click(self, by, locator): self.find(by, locator).click()
```

## Page class
```python
class HomePage(BasePage):
    SEARCH = (By.CSS_SELECTOR, "input#search")

    def search(self, text):
        self.click(*self.SEARCH)  # or send_keys if input
```

## Example test using POM
```python
def test_search(driver):
    page = HomePage(driver)
    page.search("imdb.com")
```

> 💡 Tip: Keep locators in one place; methods should express intent (not implementation).