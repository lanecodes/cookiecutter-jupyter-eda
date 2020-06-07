# Cookiecutter Jupyter EDA

[Cookiecutter][ccutter] template for exploratory data analysis in Jupyter.

Similar to [Cookiecutter Data Science][ccutter-ds] with the following differences:

- Less _stuff_. Rather than using a single project to process data and build
  models, here we focus exclusively on processing data in preparation for use in
  models ([do one thing well][one-thing-well]). The exclusion of redundant
  structure should make these projects easier to read through quickly.
- Provides a configuration file and instructions to set up a dedicated Conda
  environment (rather than `requirements.txt`) for the project. This makes the
  analysis more portable by helping others recreate the development environment.
- Adds a local Python package to the created environment which provides an
  abstraction to access data directories, e.g. `from <repo_name> import DATA_PATHS; print(DATA_PATHS.raw)`.
  This can also act as a stub from which a more developed package for the
  project can grow, easing refactoring of code out of notebooks into 
  well-organised modules.

[ccutter]: https://github.com/cookiecutter/cookiecutter
[ccutter-ds]: https://github.com/drivendata/cookiecutter-data-science
[one-thing-well]: https://en.wikipedia.org/wiki/Unix_philosophy
