@echo off
rem Run sanity test cases
echo Running sanity test cases...
pytest -m "sanity" --html=Reports/report.html TestCases/

rem Run regression test cases
echo Running regression test cases...
pytest -m "regression" --html=Reports/report_regression.html TestCases/

pause
