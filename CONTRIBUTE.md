# Contributing to PomoCLI

This document will get you started to contribute to the PomoCLI project easily, there'll be a list of the used technologies and a setup guild, also an explanation of how to make a proper Pull Request and the formatting and rules you have to follow within your code.

---

## Tech Stack

- Language: [Python](https://www.python.org/)
 This project is entirely built in Python, and most of the programming will be just Python code.
 This language is simple and easy to use which made it considered as a good language for such a simple project like this.
 Python as well have some access (limited) to the actions of the system with the `os` module and some others as well.
- Framework\Library: [click](https://pypi.org/project/click/)
 Click is one of the easiest frameworks for creating a cli tool, it's using a lot of cool features and pre-configured things out of the box so creating the interface of the cli tool isn't going to be hard at all.
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

To make a pull request you have to follow the proper way, aside from forking and committing, you need to make sure you explain the feature you add or the issue you solve very well.

### Steps of making a pull request

- Fork the repository
- Create a separate branch to make your feature or fix your bug, but you have to make sure it's based of the `develop` branch (in any other cases the pull request will be rejected, you cannot use a branch that's based on the `main` branch)
- Work on your feature or issue solving
- Make the pull request explaining everything you can.

### The pull request structure

When you make a pull request it has to be easy for us to identify what did you do by just the name, so firstly consider these naming styles:

```gitcommit
[feat]: {the feature in short terms}
[issue]: {the issue you solved} ({issue tag})
```

Where whatever within a `{}` is replaces by what it describes indeed.  

In case you're solving an issue, it must have an issue that you'll mention in your pull request name, please before making the pull request, check the issues to find an issue about it explaining the error or bug. If there was none you can create an issue giving all the data about the issue in it, then you can mention that issue in your pull request.

This is making things more clear for the maintainers, as in the pull request you'll only have to explain how the issue was solved, but the issue itself will be explained in the issue you mentioned.

You must make sure as well that there's no pull requests covering the same feature or issue. If there was you might consider helping with that pull request if you're interested in making that feature or solving that issue.

And keep in mind that tags make it easier for us to know about your pull request and get interested in including it in our project.

---

## Formatting & Linting

When you're coding to raise your opportunity of being accepted, you have to follow our formatting and linting style.
For example we prefer to have variables in snake case, and functions using camel case.
All that will be tracked by PyLint, it'll notify you about it, always consider accepting that changes to make your work into our project.

You have to format your code with Black as well to make it clear.

Not following our formatting and linting style might cause your pull request to be ignored as the maintainers need to work on cleaning your code, so they might get it done late. Help us to help you. ;)
