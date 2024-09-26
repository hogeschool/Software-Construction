# Automating tests
Automated testing is a crucial practice in software development. It helps ensure the quality, reliability, and correctness of your codebase. Let’s explore some key aspects related to automating tests.

<br>

## Tools

### Pytest
Pytest is a popular testing framework for Python. It provides a simple and efficient way to write and execute test cases. Some of its features include:

- **Concise Syntax**: Pytest allows you to write test functions using a clean and readable syntax. You can use plain Python assert statements or more advanced assertions.
- **Fixture Support**: Fixtures allow you to set up and tear down resources needed for testing (e.g., database connections, mock services). Pytest makes it easy to define and use fixtures.
- **Powerful Test Discovery**: Pytest automatically discovers and runs all test files in your project directory. No need to explicitly specify test paths.
- **Plugins**: Pytest has a rich ecosystem of plugins that extend its functionality. You can find plugins for coverage reporting, parallel test execution, and more.

If we look at our `Calculator` class, a simple unittest via the build in `unittest` of Python looked something like:
```python
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_positive_number(self):
        self.assertAlmostEqual(self.calculator.square_root(25), 5.0, places=6)

    def test_zero(self):
        self.assertAlmostEqual(self.calculator.square_root(0), 0.0, places=6)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            self.calculator.square_root(-10)


if __name__ == "__main__":
    unittest.main()
```

Running the test would be done via:
```
python test_calculator.py
```

### Converting to pytest
If we want to use `pytest`, we need to install it via `pip` the package-manager of Python.
```
pip install pytest
```

We could now convert our unittest as follow
```python
import pytest
from calculator import Calculator  # Assuming you have a Calculator class

@pytest.fixture
def calculator():
    return Calculator()

def test_positive_number(calculator):
    assert pytest.approx(calculator.square_root(25), 5.0, rel=1e-6)

def test_zero(calculator):
    assert pytest.approx(calculator.square_root(0), 0.0, rel=1e-6)

def test_negative_number(calculator):
    with pytest.raises(ValueError):
        calculator.square_root(-10)
```

We run this test by executing the following command:
```
pytest test_calculator.py
```

<br>

> Both pytest and unittest can be used and in the previous example you see no big difference, pytest uses `assert` for most testcases, which makes it easier to write. It also does not need a `if __name__ == "__main__"` that claass the test.

<br>

### Other languages
While Pytest is popular in the Python community, other programming languages also have their own testing frameworks. For example:

- NUnit/xUnit for .NET
- JUnit for Java
- Mocha for JavaScript
- *many more...*

Each of these frameworks has its unique features and conventions, but the underlying goal remains the same: to automate testing and catch issues early in the development process.

<br>

## Benefits
Automating tests offers several advantages:

**Efficiency**: <br>
Automated tests can be run quickly and repeatedly, saving time compared to manual testing.

**Consistency**: <br> 
Automated tests follow predefined steps consistently, reducing human error.

**Regression Detection**:  <br>
Automated tests catch regressions (unexpected issues introduced by code changes) early, preventing them from reaching production.

**Continuous Integration (CI)**:  <br>
Automated tests integrate seamlessly with CI/CD pipelines, ensuring that code changes don’t break existing functionality.

**Documentation**:  <br>
Test cases serve as living documentation, explaining how different parts of your application should behave.

> In summary, automating tests improves code quality, accelerates development, and provides confidence in your software.

 <br>

> :memo: **Good to know**, in the next workshop will dive deeper into the subject of test automation via GitHub Actions.