# Techniques for testing

<br>

## How about those boxes?
Let’s delve into the world of software testing techniques and explore the differences between black-box, white-box, and gray-box testing:

### Black-box
Black-box testing is a type of software testing where the functionality of the software is examined without any knowledge of its internal code or implementation. Testers focus on the software's external attributes and behavior, looking at it from the user's perspective. This type of testing is also known as functional testing, black-box testing validates the application based on requirements and test cases without considering any of the internal details.

### White-box
White-box testing is the exact opposite of black-box testing and is sometimes also referred to as glass-box testing (because you can see everything you will test). With white-box testing we examine the software by analyzing its internal data structures, physical logic flow and architecture at the source. When using white-box tests, testers view the application from the developer's standpoint, understanding the code and structure. We use white-box testing to ensure code coverage, decision paths, and logic within the application.

### Gray-box
And then there is something in between. As the name suggests it combines elements of black-box and white-box testing.
When using gray-box testing, the tester has partial access to information about the code, but not all details are known.
This form of testing is used to strike a balance between the application's behavior and its internal design, this makes it well suited for web applications.

<br>

## Where to start?
A lot of boxes, but what does it look like if you want to use one.

### Equivalence partitioning (EP)
also known as Equivalence Class Partitioning (ECP), is a black-box testing technique. It divides a range of input values into equivalence data classes. Testers select a representative input value from each defined interval of equivalence data classes. If the output for that input value is valid, the entire class interval is considered valid, and vice versa.

#### Example:
Suppose an application allows users to enter passwords of lengths between 8 and 12 characters.

We have the following equivalence classes:
* Invalid: Passwords with fewer than 8 characters.
* Valid: Passwords with lengths between 8 and 12 characters.
* Invalid: Passwords with more than 12 characters.

#### Do time!
Suppose we have a function that calculates the square root of a positive number. 
```python
import math

class Calculator:
    def square_root(self, x):
        if x <= 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)
```

We can divide the input domain into equivalence classes, fill in the blank spots
* Invalid: <blank>
* Valid: <blank>

<details markdown="1">
<summary align="right">Reveal potential answer</summary>

* Invalid: 0, -1, -100
* Valid: 4, 16, 2.25
</details>

### Boundary value analysis (BVA)
BVA focuses on testing the behavior of an application using test data that exists at boundary values.
For a given range of input data values, boundary values (extreme end values) are used for testing.
It is believed that software is most likely to fail at the upper and lower limits of input data values.

#### Example: 
Consider an application that allows people aged 20 to 50 years (both 20 and 50 inclusive) to fill out a form. 

| Invalid   |                 Valid                 |    Invalid |
| :-------- | :-----------------------------------: | ---------: |
| (min - 1) | (min, min + 1, nominal, max - 1, max) | ( max + 1) |
| 19        |          20, 21, 30, 49, 50           |         51 |

The boundary values are 20 (minimum) and 50 (maximum). Test values include:
* Invalid: Age less than 20. (minimum - 1)
* Valid: Ages 20, 21, 30, 49, and 50. (minimum, minimum + 1, nominal, maximum - 1, maximum)
* Invalid: Age greater than 50 (maximum + 1)

#### Do time!
Let’s consider a function that checks if a given year is a leap year. 
```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```
How would the following table look like?

| Invalid | Valid | Invalid |
| :------ | :---: | ------: |
| ...     |  ...  |     ... |

<details markdown="1">
<summary align="right">Reveal potential answer</summary>

| Invalid | Valid | Invalid |
| :------ | :---: | ------: |
| 3       |   4   |       5 |
| 103     |  104  |     105 |
| 399     |  400  |     401 |
| 403     |  404  |     405 |
| 1999    | 2000  |    2001 |
| 2039    | 2040  |    2041 |
</details>


### Decision table-based testing
Decision tables are used to represent complex business rules or logic.
Testers create a table with conditions (inputs) and corresponding actions (outputs).
Each combination of conditions leads to specific actions.
Decision table-based testing ensures comprehensive coverage of different scenarios.



#### Example: 
An e-commerce website’s decision table might include conditions like payment method, shipping location, and order total, leading to actions such as processing the order, applying discounts, or canceling the order.

| Condition | Payment Method   | Shipping Location | Order Total | Action                    |
| :-------- | :--------------- | :---------------- | :---------- | :------------------------ |
| 1         | Credit Card      | Domestic          | < $100      | Process the order         |
| 2         | Credit Card      | Domestic          | ≥ $100      | Apply a discount          |
| 3         | Credit Card      | International     | Any         | Cancel the order          |
| 4         | PayPal           | Any               | Any         | Process the order         |
| 5         | Bank Transfer    | Any               | Any         | Process the order         |
| 6         | Cash on Delivery | Any               | Any         | Process the order         |
| 7         | Other            | Any               | Any         | Review manually or cancel |

#### Do time!
Imagine an e-commerce website that offers discounts based on the payment method and order total.
```python
def apply_discount(payment_method, order_total):
    if payment_method == "Credit Card":
        if order_total > 100:
            return "Apply Discount"
        else:
            return "No Discount"
    elif payment_method == "PayPal":
        if order_total > 50:
            return "Apply Discount"
        else:
            return "No Discount"
    else:
        return "Invalid payment method"
```

How would the decision table look like for the above code?
<details markdown="1">
<summary align="right">Reveal potential answer</summary>

| Condition | Payment Method | Order Total | Action                 |
| :-------- | :------------- | :---------- | :--------------------- |
| 1         | Credit Card    | > $100      | Apply a discount       |
| 2         | Credit Card    | ≤ $100      | No Discount            |
| 3         | PayPal         | > $50       | Apply a discount       |
| 4         | PayPal         | ≤ $50       | No Discount            |
| 5         | Other          | Any         | Invalid payment method |

</details>
