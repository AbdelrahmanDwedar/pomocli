# Contributing to PomoCLI

This document will get you started to contribute to the PomoCLI project easily, there'll be a list of the used technologies and a setup guild, also an explanation of how to make a proper Pull Request and the formatting and rules you have to follow within your code.

---

## Tech Stack

- Language: [Python](https://www.python.org/)
	This project is entirely built in Python, and most of the programming will be just Python code.
	This language is simple and easy to use which made it considered as a good language for such a simple project like this.
	Python as well have some access (limited) to the actions of the system with the `os` module and some others as well.
- Framework\Library: [click](https://pypi.org/project/click/)
	Click is one of the easiest frameworks for creating a cli tool, it's using a lot of cool features and preconfigured things out of the box so creating the interface of the cli tool isn't going to be hard at all.
	You can read more in the documentation.
- Unit Testing: [unittest](https://docs.python.org/3/library/unittest.html)
	unittest is built-in with Python, and yet it's not bad option at all (it might look a bit harder than PyTest, but pretty much the same thing).
	Also as unittest mostly depend of OOP, we can use inheritance from our class to the testing class easily. 
- Linting: [PyLint](https://pypi.org/project/pylint/)
	PyLint by far is the most used linting tool for python, you have our own preferences for the best code.
	All that rules will be explained here and all of them are in the [pylintrc](./pylintrc).
- Formatting: [Black](https://pypi.org/project/black/)
	Black is the formatter we prefer, it's pretty much opinionated and we don't need to think twice about most of the formatting practices we use.
	Also it mostly follows the standard formatting that the Python recommend.

---

## Pull Request


