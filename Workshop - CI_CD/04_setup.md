## Setting up a CI/CD Tool

Before we start, we have to make a decision about the tool we want to use.
WIthin this course we will have free access to GitHub Actions and Gitlab
> During the workshops we will use GitHub Actions for all examples, check the documentation of the tool you use.
> 
### Popular CI/CD tools:
- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Bamboo
- Bitbucket Pipelines
- CircleCI
- Jenkins
- Travis CI

### Before you start
Make sure you have a repository ready that contains code, but also at least one unittest.

>  :TODO: If this seems like an impossible task, how about using a prepared repo for that?

Let's start by iniatializing a new Python project called `calculator`:
```shell
python3 -m venv calculator

. calculator/Scripts/activate
# . calculator/bin/activate (on Mac and Linux)
```

<br>

Open the directory `/calculator`, inside your favorite IDE.
We need to create a class file that holds soms small logic for this workshop.

This is going to be the `Calculator` class we have created earlier, create the following class inside the `calculator.py` file:

```python
class Calculator:
    def summation(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def quotient(self, a, b):
        return a / b
```
We've create a class called `Calculator`, that has 4 methods:
- `sum(a, b)`
- `differnce(a, b)`
- `product(a, b)`
- `quotient(a, b)`

<br>

If all went fine, you're `/calculator` directory should look like this:

> :question: Stuck or having problems, ask the teacher or a classmate to help you.

```
Calculator/
|
├── .git
├── .gitignore
├── README.md
└── calculator.py
```
> The .venv environment files are not present in this example, but could be present in your directory

<br><br>

### Installing dependencies and storing them for later

We're going to create some simple unittests for our class `Calculator`.
Before we can continue we need to install some dependencies for testing and reporting.
`pip` the `P`ackage `I`nstaller for `P`ython, can help us achieving this. Use the following command to install the following dependencies:
- `flake8`
- `pytest`
- `pytest-cov`

```shell
pip install flake8 pytest pytest-cov
```

<br>

Because we are going to use an automated pipeline later, we need to secure these dependencies as requirements for later.
This assures that we can test inside our pipeline as well with the same packages as we use local. To do this, we use the following command:

```shell
pip freeze > requirements.txt
```

This command `freeze`s the requirements inside the file `requirements.txt` so we can use it later to auto install these dependencies.

> :question: Stuck or having problems, ask the teacher or a classmate to help you.

<br><br>

### Let's do some checks

We're going to several checks on our created class `Calculator` and the first is a `flake8` check. This will check if our code is following the [PEP 8 guidelines](https://peps.python.org/pep-0008/). We are using the `--statistics` flag here, so we can also see how many times an error occurs. 

```shell
flake8 calculator.py --statistics

.\calculator.py:12:21: W292 no newline at end of file
1     W292 no newline at end of file
```

The report shows us that we did not complete follow the PEP 8 guidelines, we are missing a newline at the end of the file.
Add this to your `calculator.py` file, to fix this issue. You can rerun the command to make sure it is fixed.

<br>

To test our simple class `Calculator` we can create a unittest. For the purpose of this workshop we will only create 2 tests, covering 2 of the methods of our class. These will be for the methods `summation` and `difference`

```python
import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_summation(calculator):
    assert 10 == calculator.summation(5, 5)


def test_difference(calculator):
    assert 4 == calculator.difference(8, 4)

```

<br>

Let's see what the coverage is, you would expect it to be 50% right? \
Run the following command to check what the result will be `pytest -v --cov`
> :notebook: Sometimes it's needed to prepend your command with `python -m`, depending on how your packages are installed.

```shell
collected 2 items

test_calculator.py::test_summation                      PASSED  [ 50%] 
test_calculator.py::test_difference                     PASSED  [100%] 

---------- coverage: platform win32, python 3.10.11-final-0 ----------
Name                                               Stmts   Miss  Cover
----------------------------------------------------------------------
calculator.py                                         9      2    78%
test_calculator.py                                    9      0   100%
----------------------------------------------------------------------
TOTAL                                                18      2    89%
```

If we take a look at this report we can see that we have `78%` coverage on `calculator.py` and a `100%` on `test_calculator.py`.
<br>
Our overall coverage comes down to `89%` percent, which is different then the expected `50%`.

<br>

We can fix this a bit by creating a `.coveragerc` file that has some data about what to cover and what to omit:

```ini
[run]
omit = test_*
```

Running the command `pytest -v --cov` again, will now give us a cleaner report:

```shell
collected 2 items

test_calculator.py::test_summation                      PASSED  [ 50%] 
test_calculator.py::test_difference                     PASSED  [100%] 

---------- coverage: platform win32, python 3.10.11-final-0 ----------
Name                                               Stmts   Miss  Cover
----------------------------------------------------------------------
calculator.py                                         9      2    78%
----------------------------------------------------------------------
TOTAL                                                 9      2    78%
```

> The total percentage is still higher then `50%`, that is because code coverage checks on method coverage and line coverage.

An extra step we can take is adding an extra flag to the command we used, this will tell when a coverage percentage is considered a fail (and we should increase it). We could do this by adding `--cov-fail-under=90` in which we want at least 90% codecoverage.
<br>
The total command would look as follow: `pytest -v --cov --cov-fail-under=90`, if we run this now we get an extra line in the output showing us we did not pass the minimum coverage requirement:
> :notebook: Sometimes it's needed to prepend your command with `python -m`, depending on how your packages are installed.

```console
FAIL Required test coverage of 90% not reached. Total coverage: 77.78%
```

<br>

### Wrapping up

If all went well, we should have a folder looking somewhat like the following:

```
Calculator/
|
├── .coveragec
├── .git
├── .gitignore
├── README.md
├── calculator.py
├── requirements.txt
└── test_calculator.py
```

<br>

## :tada: Congratulations!

You have learnt :

1.  How to setup a Python environment
2.  How to install dependencies and save them as requirement
3.  How to check the PEP 8 style via `flake8`
4.  How to write unittest and check code coverage via `pytest --cov`
