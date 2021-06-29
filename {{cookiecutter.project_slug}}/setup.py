from setuptools import find_packages, setup
from {{cookiecutter.project_slug}}._version import __version__

requirements = [
    "wasabi",
]

setup(
    name="{{cookiecutter.project_slug}}",
    version=__version__,
    packages=find_packages(include=["{{cookiecutter.project_slug}}"]),
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    include_package_data=True,
    install_requires=requirements,
)
