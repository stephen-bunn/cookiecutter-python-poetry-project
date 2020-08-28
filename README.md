# Cookiecutter Template – Python Poetry Package 🎶🐍📦

This project contains a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template that allows us to easily build out fully intialized Python packages that are ready for publishing right out of the box. We also add in a whole bunch of tooling to benefit the development experience and promote project sustainability.

## Usage

First make sure that you have [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) installed:

```console
$ pip install --user cookiecutter
```

Then request and execute the template using:

```console
$ cookiecutter gh:stephen-bunn/cookiecutter-python-poetry-project
```

This will prompt you to enter a couple fields to understand how to generate the project.
This template will:

1. Setup the full package structure and configuration files as well as create a couple starting `__init__.py` files for the package and the corresponding tests
2. Initialize a new git repository and point the origin to the correct GitHub route
3. Build a local virtual environment with initial package testing and documentaion building dependencies
4. Install and initialize environments for necessary pre-commit hooks
5. Add all generated files to an initial commit and prompt the user to enter a valid commit message

> To learn more about the generated structure and tooling provided in this cookiecutter project template, please read through the provided [Python Project Structure](./STRUCTURE.md) documentation.

### Installing Dependencies

Because we are trying to build a packaged project, we need to install specific packages in different ways (since Python's package management structure sucks).
By following these guidelines, we can ensure that our project doesn't get too bloated and can be easily installable everywhere without having to re-declare dependencies in multiple files.

If you are installing a **development** dependency, utilize `poetry`.

```console
$ poetry add <DEPENDENCY NAME> -D
```

### Project Tasks

We have written and included a couple invoke tasks that are used as an abstraction to do many project releated tasks.
You **must** run the invoke scripts using the `poetry run invoke <TASK NAME>` or `poetry run inv <TASK NAME>` syntax.
Most of these tasks are pretty self-explanitory.

> Be cautious of modifying these tasks to a great extent. Other files and scripts (such as pre-commit hooks) depend on these tasks executing a certain way.

```console
$ poetry run invoke -l
Available tasks:

  build                  Build the project.
  clean                  Clean the project.
  profile                Run and profile a given Python script.
  test                   Test the project.
  docs.build             Build docs.
  docs.build-news        Build towncrier newsfragments.
  docs.clean             Clean built docs.
  docs.view              Build and view docs.
  package.build          Build pacakge source files.
  package.check          Check built package is valid.
  package.clean          Clean previously built package artifacts.
  package.format         Auto format package source files.
  package.requirements   Generate requirements.txt from Poetry's lock.
  package.stub           Generate typing stubs for the package.
  package.test           Run package tests.
  package.typecheck      Run type checking with generated package stubs.
```
