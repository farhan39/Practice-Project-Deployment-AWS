"""Python setup.py for practice_project_deployment_aws package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("practice_project_deployment_aws", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="practice_project_deployment_aws",
    version=read("practice_project_deployment_aws", "VERSION"),
    description="Awesome practice_project_deployment_aws created by farhan39",
    url="https://github.com/farhan39/Practice-Project-Deployment-AWS/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="farhan39",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["practice_project_deployment_aws = practice_project_deployment_aws.__main__:main"]
    },
    extras_require={
        "test": read_requirements("requirements-test.txt")
        + read_requirements("requirements-base.txt")
    },
)
