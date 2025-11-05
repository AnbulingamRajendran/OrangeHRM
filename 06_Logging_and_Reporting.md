# 06 - Logging & Reporting

## logging module setup
```python
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Starting test")

# used in irctc
    def log_generator():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=".\\Logs\\report.log", mode="w", encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                      datefmt='%d-%b-%y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
```

## Pytest HTML report
```
pytest --html=report.html --self-contained-html
```

## Allure (optional)
- Generate: `pytest --alluredir=allure-results`
- Serve: `allure serve allure-results`