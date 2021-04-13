from setuptools import find_packages, setup

__version__ = "0.1"

setup(
    name="{{cookiecutter.repo_name}}",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "{{cookiecutter.repo_name}} = {{cookiecutter.repo_name}}.__main__:cli"
        ]
    },
)
