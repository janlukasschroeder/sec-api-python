from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sec-api",
    version="1.0.31",
    author="SEC API",
    author_email="support@sec-api.io",
    description="SEC EDGAR Filings API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
    ],
    keywords=[
        "SEC EDGAR API",
        "SEC Filings API",
        "SEC Filing Search API",
        "SEC Full-Text Search API",
        "EDGAR API",
        "Finance",
        "CIK",
        "CUSIP",
        "CUSIP to Ticker",
        "CUSIP to CIK",
        "10-Q",
        "10-K",
        "8-K",
        "S-1",
        "424B4",
        "XBRL Converter",
        "Financial Statements API",
        "Insider Trading Data",
        "Executive Compensation Data",
        "Form D Offerings API",
        "Form N-PORT API",
        "Form ADV API",
        "10-K/10-Q/8-K Section Extractor API",
    ],
    project_urls={
        "Bug Reports": "https://github.com/janlukasschroeder/sec-api-python/issues",
        "Repository": "https://github.com/janlukasschroeder/sec-api-python",
        "Documentation": "https://sec-api.io/docs",
    },
)
