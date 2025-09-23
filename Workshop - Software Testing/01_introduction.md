# Introduction to Software Testing
Software testing is a crucial process in the software development lifecycle. Its primary goal is to ensure that the system and its components meet the specified requirements and work accurately in every case.

<br>

## Why test?
Testing helps uncover defects early in the development process, reducing the cost of fixing them later.

It ensures that the software behaves as expected, meets user needs, and complies with business requirements.

## Role of testing

Testing plays a crucial role in the software development process. Here are some key aspects:

#### Bug Identification and Fixing
Testing helps identify and fix bugs before the software is released, ensuring it operates as intended.

#### Quality Assurance
It ensures the software meets the required standards and functions correctly under various conditions.

#### Usability Evaluation
Testing assesses the software’s usability from the end-user’s perspective, ensuring it is user-friendly and meets user expectations.

#### Verification and Validation
It verifies that the software meets the specified requirements and validates that it fulfills its intended purpose.

#### Performance Improvement
Testing helps improve the software’s performance by identifying areas that need optimization.

#### Risk Mitigation
By identifying potential issues early, testing helps mitigate risks associated with software failures.

<br>

## Levels of testing

### 1. Unittesting
Unittesting is a method used to test software modules or individual pieces of source code (units) in isolation. Each unit is tested separately, and various test cases are executed to ensure correct behavior.

> A test that accesses a database, an API or another method wouldn’t be considered a unit test.

The goal of unittesting is to verify that functional units work independently and correctly. It aligns with modular software development principles.

Key Points:
- Unittests are typically performed by developers or testing teams.
- Unlike end-user tests, unittests focus on specific units of code.
- Benefits include catching issues during software modifications, integration, and maintaining up-to-date documentation.
- Limitations: Unittests only cover the unit itself, not system-wide interactions.

Example:
* Creating test cases for a function that calculates the square root of a number.
* Ensuring that a class method correctly handles edge cases.

```python
import math
import unittest

class Calculator:
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)


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

### 2. Integrationtesting
Integration testing sits just above unit testing in the testing pyramid. <br>
Integration testing involves testing various software modules together as a group to verify their seamless interaction.

> If you think about it, one project is likely to involve the development of many features. Sometimes, when working as a team, there are a number of developers involved. Integration testing will check that all features being developed will work together.

Approaches:
-   Big Bang Approach: All units/modules are grouped and tested as a whole.
    -   Pros: Quick results for small systems.
    -   Cons: Difficult fault localization, potential component oversight.
-   Incremental Approach:
    -   Bottom-Up: Lower-level modules are integrated and tested first.
        -   Pros: Easier fault detection, no need to wait for all units to complete.
        -   Cons: High-level components tested last.
    -   Top-Down: High-level modules tested first, followed by lower-level modules.
        -   Pros: Early prototype creation, priority-based flaw detection.
        -   Cons: Stubs needed for missing modules, inadequate lower-level testing.
- Hybrid Integrated Testing: Combines elements of both approaches.


### 3. Systemtesting
System testing validates the fully integrated software product against end-to-end specifications. It ensures that the software meets functional and non-functional requirements.

Objectives:
- Verify complete system functionality.
- Test user experience, reliability, security, and compliance.

Examples:
- Testing user account creation, product search, and checkout processes.
- Assessing system performance under load.

### 4. Acceptancetesting
Acceptance testing evaluates whether a system meets business and user requirements. It’s the final stage before software release.

Purpose:
- Verify functional and non-functional aspects.
- Performed by end users or an expected user group.

Examples:
- Successful account creation, product purchase, and checkout.
- Transaction processing rate and concurrent user handling.
