"""Package setup configuration for pomocli."""
from setuptools import setup, find_packages

setup(
    name="pomocli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click==8.1.8",
    ],
    entry_points={
        "console_scripts": [
            "pomocli = main:cli",
        ]
    },
)
