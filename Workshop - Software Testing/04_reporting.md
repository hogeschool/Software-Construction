# Reporting and Management of your tests
Effective reporting and management of software testing play a crucial role in ensuring product quality, identifying defects, and making informed decisions. Let’s explore the key aspects:

<br>

## Test Planning and Execution

### Planning
This phase involves defining the scope of testing, identifying test objectives, and creating a test plan. It includes tasks like understanding requirements, prioritizing features, and allocating resources.

### Estimation
In this step, you estimate the effort required for testing. It includes assessing the complexity of test cases, estimating execution time, and allocating resources accordingly.

### Execution
During this phase, you execute the test cases based on the test plan. It involves running tests, capturing results, and reporting any defects found.

<br>

## Metrics and Coverage

### Metrics 
Metrics provide quantitative data about the testing process. Common metrics include test case pass/fail rates, defect density, test execution time, and code coverage.

```text
======================================== test session starts ========================================
collected 3 items

test_calculator.py::TestCalculator::test_negative_number    PASSED                            [ 33%]
test_calculator.py::TestCalculator::test_positive_number    PASSED                            [ 66%] 
test_calculator.py::TestCalculator::test_zero               PASSED                            [100%] 

========================================= 3 passed in 0.28s ======================================== 
```

### Coverage 
Coverage refers to the extent to which your tests cover different aspects of the application. Types of coverage include code coverage (how much code is exercised by tests), requirement coverage (how well requirements are tested), and risk-based coverage (focusing on critical areas).

We expanded our `Calculator` example from earlier with 4 extra methods. How many CodeCoverage do you think we have with the provided test? Python has a library for this `coverage` which can be installed via: `pip install coverage`.

```python
from math import sqrt

class Calculator:
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return sqrt(x)

    def sum(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def quotient(self, a, b):
        return a / b
```

When we run the test again but now via the coverage tool `coverage run .\test_calculator.py` . This will collect all the coverage information which we can extract via the report command: `coverage report --omit="test*"`. We can see we are missing coverage on specific lines (*these are the `return` values of each added method to the class Calculator*).

```text
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
calculator.py           14      4    71%   11, 14, 17, 20
--------------------------------------------------
TOTAL                   14      4    71%
```

<br>

> :exclamation: **Test coverage is only indicative.** <br>
> It’s a great tool to reveal any gaps in your test approach, but it shouldn’t be taken as gospel. And anyway, even “perfect” test coverage doesn’t prevent new bugs from being introduced. It’s better to have really smart tests than it is to have 100% coverage!

<br>

## Reports
Test reports summarize testing activities and results. They help stakeholders (product managers, analysts, developers) understand product quality and make informed decisions. A good test report includes:
- **Test Summary**: Overview of what was tested, when, and how.
- **Defect Summary**: Details of defects found during testing.
- **Test Execution Metrics**: Pass/fail rates, execution time, etc.
- **Coverage Metrics**: Code coverage, requirement coverage, etc.
- **Recommendations**: Suggestions for improvement.
