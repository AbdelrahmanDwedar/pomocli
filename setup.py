from setuptools import setup, find_packages

setup(
    name="pomocli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "black==25.1.0",
        "click==8.1.8",
        "iniconfig==2.1.0",
        "mypy-extensions==1.0.0",
        "packaging==24.2",
        "pathspec==0.12.1",
        "platformdirs==4.3.7",
        "pluggy==1.5.0",
        "pytest==8.3.5",
        "setuptools==78.1.0",
    ],
    entry_points={
        "console_scripts": [
            "pomocli = main:cli",
        ]
    },
)
