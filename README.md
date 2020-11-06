# torch-tweaks
Utility functions for PyTorch.

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `torch-tweaks` [git repo](http://github.com/ulf1/torch-tweaks) is available as [PyPi package](https://pypi.org/project/torch-tweaks)

```
pip install torch-tweaks
pip install git+ssh://git@github.com/ulf1/torch-tweaks.git
```


## Usage
Check the [examples](http://github.com/ulf1/torch-tweaks/examples) folder for notebooks.


## Commands
Install a virtual environment

```
python3.8 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
pip install -r requirements-dev.txt --no-cache-dir
pip install -r requirements-demo.txt --no-cache-dir
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`

Clean up 

```
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```


## Debugging
* Notebooks to profile python code are in the [profile](http://github.com/ulf1/torch-tweaks/profile) folder


## Support
Please [open an issue](https://github.com/ulf1/torch-tweaks/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/torch-tweaks/compare/).
