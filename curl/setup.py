from setuptools import setup, find_packages

setup(
    name="curl",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A Python library that mimics the curl command",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author="panoscodergr",
    author_email="panoscodergr@gmail.com",
    license="MIT",
    url="https://github.com/panoscodergr/curl_lib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
