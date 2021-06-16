from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sec-api",
    version="1.0.1",
    author="SEC API",
    author_email="support@sec-api.io",
    description="SEC EDGAR Filings API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sec-api.io",
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Topic :: Software Development :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['SEC EDGAR API', 'SEC Filings API', 'EDGAR API', 'Finance', 'CIK', 'CUSIP']

)
