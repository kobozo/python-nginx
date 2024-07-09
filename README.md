# Poetry Template Project

This repository serves as a template for starting new Python projects with Poetry, pre-configured with code quality tools and pre-commit hooks.

## Getting Started

Follow these steps to set up your project:

### 1. Fork or Use This Repository as a Template

1. **Fork the Repository**:
    - Go to the [repository page](https://github.com/kobozo/python-poetry-template).
    - Click the "Fork" button on the top right to create a copy of the repository under your GitHub account.

2. **Use as a Template**:
    - Go to the [repository page](https://github.com/kobozo/python-poetry-template).
    - Click the "Use this template" button.
    - Follow the prompts to create a new repository based on this template.


### 2. Change Project Name and Author

```sh
python update-project.py <new-text> '<your-name>' <your-email>
```

example:

```sh
python update-project.py new-project 'My Name' myemail@gmail.com
```

This will update the project and remove the file update-project.py 

### 3. Install Poetry

If you haven't installed Poetry yet, follow the instructions [here](https://python-poetry.org/docs/#installation).

### 4. Install Dependencies

Navigate to the project directory and install the dependencies:

```sh
poetry install
```

This will create a virtual environment and install the necessary packages.

### 5. Set Up Pre-commit Hooks

To ensure code quality and consistency, follow these steps to install and configure pre-commit hooks:

```sh
poetry run pre-commit install
```

### 6. Update Packages to the Latest Version

To update the packages to their latest versions:

```sh
poetry update
```

This will update all dependencies in your pyproject.toml file to their latest compatible versions.

## Configuration

### Default Python Version

The default Python version is set to 3.11 in the pre-commit configuration. If you need to change this, update the `default_language_version` in the `.pre-commit-config.yaml` file.

### Pre-commit Hooks

The pre-commit hooks configured in this template include:

- **[Black](https://github.com/psf/black)** for code formatting.
- **[Pydocstyle](https://github.com/PyCQA/pydocstyle)** for enforcing docstring conventions.
- **[Pycln](https://github.com/hadialqattan/pycln)** for removing unused imports.
- **[Trailing Whitespace](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace)** to check for and remove trailing whitespace.
- **[Check JSON](https://github.com/pre-commit/pre-commit-hooks#check-json)** to validate JSON files.
- **[Check YAML](https://github.com/pre-commit/pre-commit-hooks#check-yaml)** to validate YAML files.
- **[Check Added Large Files](https://github.com/pre-commit/pre-commit-hooks#check-added-large-files)** to ensure large files are not committed.
- **[Mypy](https://github.com/pre-commit/mirrors-mypy)** for type checking.
- **[Gitleaks](https://github.com/zricethezav/gitleaks)** for detecting secrets.
- **Unit Tests** to run tests using pytest.

You can customize these hooks by editing the `.pre-commit-config.yaml` file.

### Manually Run Pre-commit Hooks

To manually run all the pre-commit hooks on your codebase, use:

```sh
poetry run pre-commit run
```

This command runs the pre-commit hooks on the files that have been changed since the last commit.

To run the pre-commit hooks on all files in the repository, use:

```sh
poetry run pre-commit run --all-files
```

This command is useful when you want to apply the hooks to the entire codebase, ensuring all files meet the defined code quality and formatting standards.

## Running Unit Tests

To run unit tests:

```sh
poetry run pytest
```

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or if you encounter any bugs.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
