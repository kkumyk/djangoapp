## Project Setup with [Poetry](https://python-poetry.org/docs/cli)

1. [create a new poetry project](https://realpython.com/dependency-management-python-poetry/#create-a-new-poetry-project);
2. Create [virtual env](https://medium.com/@AgnesMbiti/creating-a-python-virtual-environment-on-ubuntu-22-04-5efc173ce655) and activate it;
3. use <i>[poetry add](https://realpython.com/dependency-management-python-poetry\/#declare-runtime-dependencies)</i> django command to add django latest version to the pyproject.toml file; this command does also installs django in the virtual env;

<hr>
-<i>pyproject.toml</i> lists all the project dependencies;

-<i>poetry.lock</i> keeps all the project dependencies constant so that if other people want to use your project, they will be able to install the exact same versions;