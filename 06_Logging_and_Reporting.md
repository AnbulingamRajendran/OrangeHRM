# 06 - Logging & Reporting

## logging module setup
```python
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Starting test")
```

## Pytest HTML report
```
pytest --html=report.html --self-contained-html
```

## Allure (optional)
- Generate: `pytest --alluredir=allure-results`
- Serve: `allure serve allure-results`