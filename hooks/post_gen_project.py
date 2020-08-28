# -*- encoding: utf-8 -*-
# Copyright (c) 2020 Stephen Bunn <stephen@bunn.io>
# ISC License <https://opensource.org/licenses/isc>

import os
import shutil

# initialize git repository
os.system("git init")
os.system(
    "git remote add origin "
    "git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git"
)

# initialize virtual environment for local development
poetry_command = "poetry install"
os.system(poetry_command)

# initialize pre-commit hooks
os.system("poetry run pre-commit install")

# prompt initial commit
os.system("git add --all")
os.system("git commit --signoff")
