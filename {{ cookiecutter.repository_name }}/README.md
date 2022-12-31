<h1>{{ cookiecutter.project_name }}</h1>

<p align="left">
    <a href="https://www.python.org/downloads/"><img alt="Python" src="https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg"></a>
</p>

{{ cookiecutter.project_description }}

**Table of contents**

- [Package installation](#package-installation)
- [Quickstart tips](#quickstart-tips)
- [Development installation](#development-installation)
  - [Update the dependencies](#update-the-dependencies)
  - [Build an executable for Windows (.exe)](#build-an-executable-for-windows-exe)
- [Project structure](#project-structure)

## Package installation

```bash
pip install git+https://github.com/{{ cookiecutter.repository_user }}/{{ cookiecutter.repository_name }}.git
```


## Quickstart tips

- Follow a development workflow structure:
    1. Open an Issue describing your implementation.
    2. Create a Branch called `issue-number_developer-name_problem` (e.g. `12_fernando_modify-docs`) (please don't commit directly to `master` branch). Commit from here.
    3. Create a Pull Request to `main` or `develop` branch when code were ready.
- Don't upload big files here (only tests/examples if needed). Instead, use Azure.
- The `Makefile` contains some useful command line orders (e.g. `make check`). Check it.
- Read the `CONTRIBUTING.md` if you are interest to contribute with this repository.


## Development installation

<details>
<summary>Remember to install mamba!</summary>
<pre><code>conda install -c conda-forge mamba
</code></pre>
</details>

Setup the development environment:

```bash
git clone git@github.com:{{ cookiecutter.repository_user }}/{{ cookiecutter.repository_name }}.git
cd {{ cookiecutter.repository_name }}
mamba env create -f environment.yml
conda activate {{ cookiecutter.conda_env_name }}
pre-commit install
```

Run the tests:

```bash
pre-commit run --all-files
pytest -v
```

### Update the dependencies

Re-install the project in edit mode:

```bash
pip install -e .[dev]
```

### Build an executable for Windows (.exe)

If user wants to run the packaged app without installing a Python interpreter or any modules, install [`pyinstaller`](https://pyinstaller.org/en/stable/usage.html) and execute this CLI:

```sh
# MY_SCRIPT=script_location # uncomment with script to be packaged
# MY_ICON=favicon_location # uncomment with favicon to be used within the .exe

pip install pyinstaller
pyinstaller \
    --noconfirm \
    --onefile \
    --windowed \
    --icon $MY_ICON \
    --name {{ cookiecutter.repository_name }}  $MY_SCRIPT
```

## Project structure

```sh
├── data                            <- Data used for the project.
├── Dockerfile                      <- Dockerfile for building the image.
├── docs                            <- Documentation.
│   ├── index.md -> ../README.md    <- Symlink to the README.md file.
│   └── overrides                   <- Overrides for the mkdocs-material theme.
│       └── main.html               <- Custom HTML template for the documentation.
├── environment.yml                 <- The conda environment file.
├── LICENSE -> ../LICENSE           <- License file.
├── Makefile                        <- Makefile with commands like `make data` or `make train`.
├── mkdocs.yml                      <- Configuration file for MkDocs.
├── pyproject.toml                  <- Definition of build process of the package.
├── README.md                       <- README with info of the project.
├── setup.cfg                       <- Configuration details of the python package.
├── setup.py                        <- Minimal setup dependencies.
├── src/                            <- Source dir.
│   └── my_package/                 <- Python package directory.
│       ├── __init__.py             <- This makes the directory a package.
│       └── run.py                  <- Example module.
└── tests                           <- Tests directory.
    ├── __init__.py                 <- This makes the directory a package.
    └── test_run.py                 <- Example test.
```
