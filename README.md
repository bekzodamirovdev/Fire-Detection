# Fire Detection Project

YOLO-based fire detection Django project.

## What to include / ignore
- Large files (model weights `ml_models/*.pt`): do NOT commit these directly to the repo unless you use Git LFS.
- Use GitHub Releases or external storage for model files if you don't want LFS.
- `.gitignore` is already configured to ignore `env/`, `db.sqlite3`, and `ml_models/*.pt` by default.

## Quick steps to publish to GitHub (PowerShell)

1) Activate virtual environment:
```powershell
cd C:\Users\Jaloliddin_PC\OneDrive\Desktop\fire_detection_project
.\env\Scripts\Activate.ps1
```

2) Initialize repository (run once):
```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit"
```

3a) Create GitHub repo with `gh` CLI and push (recommended):
```powershell
# install GitHub CLI and authenticate: https://cli.github.com/
gh repo create <USERNAME>/<REPO_NAME> --public --source=. --remote=origin --push
```

3b) Or create repo on GitHub website and add remote then push:
```powershell
git remote add origin git@github.com:<USERNAME>/<REPO_NAME>.git
git push -u origin main
```

## If you want to include model weights using Git LFS
```powershell
# install git-lfs
git lfs install
# start tracking weights
git lfs track "ml_models/*.pt"
# commit the .gitattributes then add and commit weights
git add .gitattributes
git add ml_models/*.pt
git commit -m "Add model weights via LFS"
git push origin main
```

## Helpful tips
- If you need me to run the `git init` / `git add` / `git commit` here, I can do it for you — confirm and I'll run the commands.
- If you want me to create the GitHub remote using the `gh` CLI, I'll need your confirmation and `gh` installed and authenticated on this machine.

