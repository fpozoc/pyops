FROM continuumio/miniconda3
WORKDIR /src/{{ cookiecutter.project_name }}
COPY environment.yml /src/{{ cookiecutter.project_name }}/
RUN conda install -c conda-forge gcc python={{ cookiecutter.python_version }} \
    && conda env update -n base -f environment.yml
COPY . /src/{{ cookiecutter.project_name }}
RUN pip install -e .[dev]
ENTRYPOINT ["make", "test"]