@echo off
rem Run sanity test cases
echo Running sanity test cases...
pytest -v -s -m "sanity" --html=Reports/report.html TestCases/

rem Run regression test cases
echo Running regression test cases...
pytest -v -s -m "regression" --html=Reports/report_regression.html TestCases/

pause
