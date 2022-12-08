import re

import setuptools

PACKAGE_NAME = "sdap_collection_manager"

with open('../VERSION.txt', 'r') as f:
    __version__ = f.readline()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    pip_requirements = f.readlines()

setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author="Apache - SDAP",
    author_email="dev@sdap.apache.org",
    description="a helper to ingest data in sdap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apache/incubator-sdap-ingester",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=pip_requirements
)
