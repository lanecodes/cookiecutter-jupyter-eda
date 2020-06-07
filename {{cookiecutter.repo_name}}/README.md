# {{ cookiecutter.project_name }}

{{ cookiecutter.tag_line }}

## Setup

### Recommended setup

The recommended way to run this analysis is to create a dedicated Conda
environment. To do this set your working directory to the directory containing
this `README` and run

```bash
conda env create -f {{cookiecutter.repo_name}}_env.yml
```

This will create a new Conda environment called `{{cookiecutter.repo_name}}`.
Activate it using

```bash
conda activate {{cookiecutter.repo_name}}
```

### Minimal setup

If you would prefer to avoid creating a new Conda environment (or avoid using
Conda entirely) you can `pip` install the package corresponding to this project
into an existing Python environment. To do this, navigate to the directory
containing this file and run

```bash
pip install -e .
```

This will install the local Python package in the Python environment currently
active in your shell. Note that the use of the `-e` flag means you can make
changes to the code in `./{{cookiecutter.repo_name}}` and these will be reflected
in any notebooks using it following a `reload` of the import, without needing to
reinstall the package.

## Project structure

```
.
├── data
│   ├── interim               <- Caches for intermediate data processing steps
│   ├── processed             <- Processed data for reporting/ visualisation
│   └── raw                   <- Original data, considered immutable
├── eda_tmp_env.yml            <- Conda environment file
├── LICENSE
├── notebooks                  <- Jupyter notebooks containing core analysis
├── README.md
├── reports
│   └── figures
├── setup.py
└── {{cookiecutter.repo_name}}          <- Python modules specific to this project
    ├── config.py              <- Project configuration code
    └── __init__.py
```

This repository uses [`cookiecutter-jupyter-eda`][cc-jupyter-eda] for basic
project structure.

[cc-jupyter-eda]: https://github.com/lanecodes/cookiecutter-jupyter-eda

## Contributors

- {{cookiecutter.author_name}} \<{{cookiecutter.author_email.replace('@', ' [at] ')}}\>
