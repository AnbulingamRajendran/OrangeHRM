# 10 - Appium (Mobile Automation)

## Setup & desired capabilities (Android)
```python
from appium import webdriver
caps = {
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "appPackage": "com.example.app",
  "appActivity": "com.example.MainActivity"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
```

## Element interactions
```python
driver.find_element_by_accessibility_id("Login").click()
driver.swipe(100,500,100,100,500)
```

## Gestures (TouchAction)
```python
from appium.webdriver.common.touch_action import TouchAction
TouchAction(driver).press(x=100,y=500).move_to(x=100,y=100).release().perform()
```

## Real device vs Emulator
- Real device: more reliable for sensors; emulator: faster for CI.
- Use device farm for scale (BrowserStack, Sauce Labs).

## Parallel testing
- Use multiple Appium servers or cloud device providers.