# 07 - Git & GitHub

## Common commands
```bash
git init
git add .
git commit -m "msg"
git push origin main
git checkout -b feature/xxx
```

## .gitignore (recommended example)
```gitignore
# Python
__pycache__/
*.py[cod]
.venv/
venv/
# IDE
.idea/
.vscode/
# Config
conf.ini
*.env
# Reports
Reports/
allure-results/
screenshots/
```

## Branching workflow
- Use feature branches, PRs, code review.
- Rebase vs merge: prefer feature branches & merge after review.

## Merging & resolving conflicts
- If files were tracked before .gitignore, remove them from tracking:
```bash
git rm -r --cached .idea venv Reports configuration/conf.ini
git commit -m "Stop tracking ignored files"
git push
```

> 💡 Tip: Keep `README.md` and contributing notes up to date.