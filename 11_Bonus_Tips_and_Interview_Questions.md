# 11 - Bonus: Tips & Interview Questions

## Common interview questions (short answers)
- **What is a shadow DOM?** A scoped DOM tree encapsulated inside a host element; normal CSS/XPath can't cross it.
- **Why use POM?** Separation of concerns; easier maintenance.
- **How to handle flaky tests?** Add proper waits, avoid hard sleeps, isolate test data, retry on transient failures.

## IRCTC automation tips (your project)
- Use session fixtures for login, and parameterize passenger data.
- Use screenshots for failure debugging.
- Use headless for CI and headed for local debugging.

## Debugging checklist
- Check element locators in DevTools.
- Try printing innerHTML via `execute_script`.
- Use `pytest -k testname -s` to see logs live.

> 🎯 Good luck with interviews — add notes here after each real interview to improve the cheatsheet!