from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    version='0.0.1',
    description='{{ cookiecutter.tag_line }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    license='{% if cookiecutter.license == 'MIT' %}MIT{% elif cookiecutter.license == 'GPLv3' %}GPLv3{% endif %}',
)
