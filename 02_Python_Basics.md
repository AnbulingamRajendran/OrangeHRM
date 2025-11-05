# 02 - Python Basics Refresher

Short examples you’ll use in automation scripts.

## Lists, Sets, Dicts
```python
# list
items = [1,2,3]
# set
s = set(items)
# dict
d = {'name':'anbu', 'role':'QA'}
```

## Loops & Comprehensions
```python
for i in items:
    print(i)

squared = [x*x for x in items]
```

## OOP (very brief)
```python
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)
```

> 💡 Tip: Keep helper utilities small and reusable (e.g., wait helpers, element wrappers).