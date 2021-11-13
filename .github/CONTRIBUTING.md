# Contributing

In this project, in order to provide a experimence of contributing to a real open-source project, we try to structure each assignment. Therefore, every contribution to this course must meet the requirements.

This contributing guide will express our expectation in your code.

---

## Style

When contributing your code, it is required to keep it organized and clean in order to make it easier to make it easier to debug, optimize, and document. To help with this process, we utilize required formatting on all assignments .

Coding style will need to be checked as part of the continuous integration of the project. You can do so by running the `flake8` and `pycodestyle` (pep8) linter in your home directory:

```bash
flake8
```

And

```bash
pycodestyle
```

We also recommend setting up your editor or IDE to highlight other style issues.

💡 Read more about [`flake8`](https://flake8.pycqa.org/en/latest/) and [`pycodestyle`](https://pycodestyle.pycqa.org/en/latest/) at their docs.

## Testing

Each assignment has a series of tests that require your code to pass. These tests are in the `./tests/` directory and are in the pytest format (https://docs.pytest.org/en/stable/). Any function in that directory with the word test in its name is run as part of the test suite. Each assignment has 4 task groups that you will need to pass.

```bash
pytest tests
```

In addition to running a full task which runs all of the tests, you can run tests in a single file with:

```bash
pytest tests/test_operators.py
```

Pytest will hide all print statements unless a test fails.

---

## For contributor

### Documentation

Throughout the codebase, we require to document all functions in a standardized style. Documentation is critical for our Python codebase, and we use it to convey requirements on many functions. Functions should have docstrings in the following form (known as Google docstyle):


```python
def index(ls, i):
    """
    List indexing.

    Args:
        ls (list): A list of any type.
        i (int): An index into the list

    Returns:
        Value at ls[i].
    """
    ...
```

A full description of this docstyle is listed here https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html.

The project also requires that you keep documentation up-to-standard throughout. Lint errors will be thrown if your documentation is in the incorrect format.

### Continuous Integration (CI)

In addition to local testing, the project is set up such that on each code push, tests are automatically run and checked on the server. You are able to see how well you are doing on the assignment by committing your code, pushing to the server, and then logging in to GitHub. This process takes several minutes, but it is an easy way to keep track of your progress as you go.

Specifically, you can run:

```bash
git commit -am "First commit"
git push origin master
```

Then go to your GitHub and click on "Pull requests". Clicking on the request itself gives a link to show the current progress of your work.
