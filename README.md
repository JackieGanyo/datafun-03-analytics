# datafun-03-analytics

Professional analytics project using Git, Python, venv, pip, and VS Code to read and process data.
Commands were used on a Windows machine running PowerShell.  

## Create and Activate Project Virtual Environment

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r "requirements.txt"
```

## Freeze Requirements

```shell
py -m pip freeze > requirements.txt
```

## Git Add / Commit / Push

```shell
git add .
git commit -m "add .gitignore, commands to README.md"
git push -u origin main
```

## Specification

This project was built to the following specification:

- [datafun-03-spec](https://github.com/denisecase/datafun-03-spec)

## Step By Step of process

## Environment Setup

1. reate and activate a Python virtual environment for the project.
2. Install all required packages into your local project virtual environment.
3. After installing the required dependencies, redirect the output of the pip freeze command to a requirements.txt file in your root project folder.
4. Document the process and commands you used in your README.md.
5. Add a .gitignore file to your project to exclude the virtual environment folder, your .vscode settings folder, and any other files that do not need to be committed to GitHub.
6. Terminal Commands: Windows example - record your process in your README:

\\\
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install requests
py -m pip freeze > requirements.txt
\\\
