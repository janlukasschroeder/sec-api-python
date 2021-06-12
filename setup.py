from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sec-api",
    version="0.0.1",
    author="SEC API",
    author_email="support@sec-api.io",
    description="SEC EDGAR Filings API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janlukasschroeder/sec-api-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
