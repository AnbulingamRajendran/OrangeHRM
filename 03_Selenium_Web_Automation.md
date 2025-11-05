# 03 - Selenium Web Automation

## WebDriver setup (Chrome)
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com")
```

## Locators
- By.ID, By.NAME, By.CSS_SELECTOR, By.XPATH, By.TAG_NAME, By.CLASS_NAME

## Waits
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
el = wait.until(EC.presence_of_element_located((By.ID, "username")))
```

## Frames, Windows, Alerts
```python
driver.switch_to.frame('frame_name')
driver.switch_to.default_content()

driver.switch_to.window(window_handle)
alert = driver.switch_to.alert
alert.accept()
```

## Shadow DOM (practical helper)
You cannot use normal `find_element` across shadow boundaries. Use JS to traverse inside shadow roots.
```python
def find_in_shadow(driver, selectors):
    # selectors: list like ['ntp-app','cr-searchbox','#input']
    script = "let root = document;
"
    for sel in selectors:
        script += "root = (root.querySelector('%s') || root).shadowRoot || root.querySelector('%s') || root;
" % (sel, sel)
    script += "return root;"
    return driver.execute_script(script)

# Example: access input inside nested shadow roots
js = '''
const outer = document.querySelector('ntp-app').shadowRoot;
const inner = outer.querySelector('cr-searchbox').shadowRoot;
return inner.querySelector('#input');
'''
el = driver.execute_script(js)
el.send_keys("imdb.com")
```

## Scrolling & Actions
```python
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(el).perform()
driver.execute_script("arguments[0].scrollIntoView(true);", el)
```

## File upload
```python
driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys("/path/to/file")
```

## Headless
```python
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.headless = True
driver = webdriver.Chrome(options=opts)
```

## Common errors & fixes
- `ElementNotInteractableException` → wait or scroll into view.
- `StaleElementReferenceException` → re-find the element after DOM update.