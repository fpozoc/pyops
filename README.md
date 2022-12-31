<h1>Python devops project template</h1>

<details><summary>Table of contents</summary>

- [Template features](#template-features)
- [Get started](#get-started)
- [Features](#features)
- [Author information](#author-information)
- [Release History](#release-history)
- [Contributing](#contributing)
  - [Branching (internal collaboration)](#branching-internal-collaboration)
  - [Forking (external collaboration)](#forking-external-collaboration)
- [License](#license)

</details>

## Template features

Using this template will help you with

- Providing a **starting point** for Python-based projects.
- Generating a **common project structure** easy to maintain.
- Following **best practices** in terms of code quality, documentation, testing, and deployment.

This template has been designed to be:

- **Simple**: Everybody within the team should be able to understand and use it.
- **Flexible**: From this starting point, the user can add or remove features as needed. For example, to create a web app, or to develop a data science project, this template can be used as a starting point.
- **Colaborative**: Propose new features, report bugs, and contribute to the template from the Issues section will be highly valuable for the team.

## Get started

If you already know [cookiecutter](https://github.com/cookiecutter/cookiecutter), just generate your project with:

```bash
cookiecutter https://github.com/fpozoc/pyops
```

<details>
<summary>Otherwise</summary>
Cookiecutter manages the setup stages and delivers to you a personalized ready to run project. To install cookiecutter, you can use pip:

<pre><code>python -m pip install cookiecutter
</code></pre>
</details>

## Features

- Environment manager: [`conda`](https://conda.io/projects/conda/en/latest/index.html) and [`mamba`](https://mamba.readthedocs.io/en/latest/) (a reimplementation of conda in C++).
- Project configuration: [`pyproject.toml`](https://github.com/fpozoc/pyops/blob/main/%7B%7B%20cookiecutter.repository_name%20%7D%7D/pyproject.toml), [`setup.cfg`](https://github.com/fpozoc/pyops/blob/main/%7B%7B%20cookiecutter.repository_name%20%7D%7D/setup.cfg) and minimal [`setup.py`](https://github.com/fpozoc/pyops/blob/main/%7B%7B%20cookiecutter.repository_name%20%7D%7D/setup.py).
- Testing with [`pytest`](https://docs.pytest.org/en/7.1.x/).
- Code formatting with [`black`](https://black.readthedocs.io/en/stable/) for as code formatter and [`pre-commit`](https://pre-commit.com/) for managing and maintaining pre-commit hooks.
- Import sorting with [`isort`](https://pycqa.github.io/isort/) sorts imports alphabetically, and automatically separated into sections and by type.
- Linting with [`pylint`](https://pylint.pycqa.org/en/latest/) checks coding style (PEP8), programming errors and cyclomatic complexity.
- Typing with [`mypy`](http://mypy-lang.org/).
- CI/CD with [`GitHub Actions`](https://github.com/features/actions).
- Automatization with [`Makefile`](https://github.com/fpozoc/pyops/blob/main/%7B%7B%20cookiecutter.repository_name%20%7D%7D/Makefile).
- Documentation and site generation with [`mkdocs`](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), a fast, simple and downright gorgeous static site generator.
- Containerize some parts of the project with [`Dockerfile`](https://github.com/fpozoc/pyops/blob/main/%7B%7B%20cookiecutter.repository_name%20%7D%7D/Dockerfile).
- Ready to use [`.editorconfig`](https://editorconfig.org/) to maintain consistent coding styles for multiple developers, [`.dockerignore`](https://docs.docker.com/engine/reference/builder/#dockerignore-file) and [`.gitignore`](https://github.com/github/gitignore/blob/main/Python.gitignore) for exclude large or sensitive files.

## Author information

Fernando Pozo (@fpozoca – fpozoc@gmx.com)

## Release History

- v0.0.1
  - Work in progress

## Contributing

Instructions to contribute to this project:

### Branching (internal collaboration)

Read [CONTRIBUTING.md](https://github.com/fpozoc/pyops/blob/main/CONTRIBUTING.md)

### Forking (external collaboration)

1. Fork it (<https://github.com/fpozoc/pyops>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

Distributed under the GNU General Public License v3.0.

See `LICENSE` [file](LICENSE).