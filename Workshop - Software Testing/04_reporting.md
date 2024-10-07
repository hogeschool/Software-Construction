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

test_calculator.py::TestCalculator::test_add                PASSED                            [ 50%]
test_calculator.py::TestCalculator::test_subtract           PASSED                            [100%] 

========================================= 2 passed in 0.28s ======================================== 
```

### Coverage 
Coverage refers to the extent to which your tests cover different aspects of the application. Types of coverage include code coverage (how much code is exercised by tests), requirement coverage (how well requirements are tested), and risk-based coverage (focusing on critical areas).

We expanded our `Calculator` example from earlier with 2 extra methods. How many CodeCoverage do you think we have with the provided test? Python has a library for this `coverage` which can be installed via: `pip install coverage`.

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
```

When we run the test again but now via the coverage tool `coverage run .\test_calculator.py` . This will collect all the coverage information which we can extract via the report command: `coverage report --omit="test*"`. We can see we are missing coverage on specific lines (*these are the `return` values of each added method to the class Calculator*).

```text
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
calculator.py      11      4    64%   9, 12-14
---------------------------------------------
TOTAL              11      4    64%
```

<br>

> :exclamation: **Test coverage is only indicative.** <br>
> It’s a great tool to reveal any gaps in your test approach, but it shouldn’t be taken as gospel. And anyway, even “perfect” test coverage doesn’t prevent new bugs from being introduced. It’s better to have really smart tests than it is to have 100% coverage!

We can also run the test coverage over multiple files, for unittest we can use the command `unittest disover -s <source_folder>` to grab all test files in that folder. <br>
To run the coverage and generate a report we will use `coverage run -m unittest discover -s .`. This will tell us, we have 4 tests in total at this moment resulting in the followin coverage report:
> If you want to run pytest with coverage you can use: `coverage run -m pytest`

```text
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
api.py             27      7    74%   28-29, 34-38
calculator.py      11      4    64%   9, 12-14
---------------------------------------------
TOTAL              38     11    71%
```

<br>

### Adjusting our tests
----

We can adjust our unittest first, by implementing more testcases:
- test multiplication
- test division
- test division by zero

<br>

**Do time!** Convert the above testcases into a working unittest.

<details markdown="1">
<summary align="right">Reveal potential solution</summary>
    
```python
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)
```
</details>
<br>

If the adjustment was correct we should see that the coverage has gone up for `calculator.py` but we are still missing coverage for our api:

```text
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
api.py             27      7    74%   28-29, 34-38
calculator.py      11      0   100%
---------------------------------------------
TOTAL              38      7    82%
```

<br>
<br>

Adjusting the `Calculator` class also resulted in an adjusted api file, the following endpoints are added:

```python
...
@app.post("/multiply")
async def multiply(data: OperationData):
    result = calculator.multiply(data.a, data.b)
    return {"result": result}


@app.post("/divide")
async def divide(data: OperationData):
    try:
        result = calculator.divide(data.a, data.b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
...
```

<br>

In the previous integration test we only covered the request itself. To adjust the integration test, we setup the following testcases:
- Validate new endpoints (multiply, divide)
- Validate zero division error
- Validate response code 200 (correct request)
- Validate response code 400 (divide by zero request)

**Do time!** Convert the above testcases into an adjusted integrationtest

<details markdown="1">
<summary align="right">Reveal potential solution</summary>

```python
class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_add(self):
        response = self.client.post("/add", json={"a": 1, "b": 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 3})

    def test_subtract(self):
        response = self.client.post("/subtract", json={"a": 5, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 2})

    def test_multiply(self):
        response = self.client.post("/multiply", json={"a": 3, "b": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 12})

    def test_divide(self):
        response = self.client.post("/divide", json={"a": 10, "b": 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 5})

    def test_divide_by_zero(self):
        response = self.client.post("/divide", json={"a": 10, "b": 0})
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())
        self.assertIn("divide by zero", response.json().get("detail"))
```
</details>

<br><br>

Now our coverage report should look like the following:

```text
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
api.py             27      0   100%
calculator.py      11      0   100%
---------------------------------------------
TOTAL              38      0   100%
```

<br>

## Reports
Test reports summarize testing activities and results. They help stakeholders (product managers, analysts, developers) understand product quality and make informed decisions. A good test report includes:
- **Test Summary**: Overview of what was tested, when, and how.
- **Defect Summary**: Details of defects found during testing.
- **Test Execution Metrics**: Pass/fail rates, execution time, etc.
- **Coverage Metrics**: Code coverage, requirement coverage, etc.
- **Recommendations**: Suggestions for improvement.
