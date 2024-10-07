# Refactoring in practice

## Recognizing "dirty" code
If Clean Code is

- Well-documented
- Well-tested
- Easy to read
- Easy to adjust
- Easy to extend

then you could define "dirty" code as the opposite; code that is not documented and tested, and is hard to read and maintain.

## Turning Dirty into Clean code
This is harder than it seems. First of all you need to recognize "dirty" code and then you also have to know how to refactor it into "clean" code. This takes years of practice, so that's why we should start practicing right away.

### Activity
The code below is functionally correct but it can be cleaned up.

1. Rewrite the following to make it more readable:

    ```python
    # Function to check if number is prime
    def is_prime(number):
        # Check if the number is less than 2
        if number < 2:
            # If less than 2 then not a prime number
            return False
        # At least one devisor must be less than the square root,
        # so we can stop early
        for n in range(math.sqrt(number)):
            # Check if the number is divisible by n
            if number % n == 0:
                # If divisible then not a prime number
                return False
        # After all checks, if not divisible by any n, then number is prime
        return True
    ```

    <details markdown="1">
    <summary align="right">
    Solution: only use comments that clarify
    </summary>

    ```python
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        # At least one devisor must be less than the square root,
        # so we can stop early
        for n in range(math.sqrt(number)):
            if number % n == 0:
                return False
        return True
    ```
    </details>

    <br><br>

1. Rewrite the following to make it more readable:

    ```python
    price = 100
    if transactionType == 1:
        price *= 1.1
    ```
    <details markdown="1">
    <summary align="right">
    Solution: be explicit, don't use magic numbers
    </summary>
    <br>

    ```python
    VAT_APPLICATION_TYPE = 1
    VAT_MULTIPLIER = 1.1

    price = 10
    if transactionType == VAT_APPLICATION_TYPE:
        price *= VAT_MULTIPLIER
    ```
    </details>

    <br><br>

2. Rewrite the following to make it more readable:

    ```python
    def process_user(usr):
        if usr != None:
            if usr.has_subscription:
                if usr.age >= 18:
                    show_full_version()
                else:
                    show_child_friendly_version()
            else:
                raise Exception('User needs a subscription')
        else:
            raise Exception('User not defined')
    ```
    <details markdown="1">
    <summary align="right">
    Solution: the early termination programming style
    </summary>
    <br>

    ```python
    def process_user(user: User) -> None:
        if user == None:
            raise Exception('User not defined')
        if not user.has_subscription:
            raise Exception('User needs a subscription')
        if user.age < 18:
            show_child_friendly_version()
        else:
            show_full_version()
    ```
    </details>

    <br>

3. Rewrite the following to make it more readable:

    ```python
    MIN_PASSWORD = 6

    def check_password_length(pw):
        return len(pw) >= MIN_PASSWORD
    ```

    <details markdown="1">
    <summary align="right">
    Solution: be more explicit
    </summary>
    <br>

    ```python
    MIN_PASSWORD_LENGTH = 6

    def is_password_long_enough(password: str) -> bool:
        return len(password) >= MIN_PASSWORD_LENGTH
    ```
    </details>

    <br>

4. Rewrite the following to make it more maintainable:

    ```python
    def log_signin():
        print(f'User signed in at {datetime.now()}')
    
    def log_singout():
        print(f'User signed out at {datetime.now()}')
    
    def log_signup():
        print(f'User signed up at {datetime.now()}')
    ```
    <details markdown="1">
    <summary align="right">
    Solution: prevent duplication or the DRY (Don't Repeat Yourself) principle
    </summary>
    <br>

    ```python
    def log_action(action: str) -> None:
        print(f'User signed {action} at {datetime.now()}')
    ```

    </details>
    <br><br>

5. Rewrite the following to do less work:

    ```python
    def get_uppercase(input):
        result = ''
        try:
            result = input.upper()
        except:
            raise Exception('Input is not of type string')
        return result
    ```
    <details markdown="1">
    <summary align="right">
    Solution: terminate early, don't do unnecessary work
    </summary>
    <br>

    ```python
    def get_uppercase(input_value: str) -> str:
        if !isinstance(input_value, str):
            raise Exception('Input value is not of type string')
            
        return input_value.upper()
    ```

    </details>
    <br><br>

6. Rewrite the following to be less coupled:

    ```python
    area = 100

    def calculate_and_update_area(radius):
        new_area = math.pi * radius * radius
        global area
        area = new_area
        
        return new_area
    
    calculate_and_update_area(5)
    ```

    <details markdown="1">
    <summary align="right">
    Solutions: let a function do one thing, single responsibility principle
    </summary>
    <br>

    ```python
    area = 100

    def calculate_area(radius: float|int ) -> float:
        return math.pi * radius * radius
    
    area = calculate_area(5)
    ```
    </details>
    <br><br>

### Warning
Please be aware that these examples were constructed and that code "in the wild" may be only partly "dirty". Also, it may be a matter of taste to consider code as "dirty":

**Example 1**

Loop version:

```python
numbers = [1,2,3,4,5,6,7,8]
odd_numbers = []
for item in numbers:
  if item % 2 == 1:
    odd_numbers.append(item)
print(odd_numbers)
```

List comprehension:

```python
numbers = [1,2,3,4,5,6,7,8]
odd_numbers = [item for item in numbers if item % 2 == 1]
print (odd_numbers)
```

It is true that the list comprehension is more compact, but if also requires a fair amount of Python knowledge to... comprehend this construction (no pun intended).

<br>

**Example 2**

Suppose we have these two functions:

```python
def calculate_discount(price):
    # Apply a 10% discount
    return price * 0.1

def calculate_tax(price):
    # Apply a 10% tax
    return price * 0.1
```

This seems to suggest that we are repeating ourselves so we may be tempted to rewrite this into

```python
def calculate_10_percent(price):
    return price * 0.1

def calculate_discount(price):
    # 10% discount
    return calculate_10_percent(price)

def calculate_tax(price):
    # 10% tax
    return calculate_10_percent(price)
```

But is this really better code? What if the discount and tax rate start to deviate? In this case we have taken the DRY principle too far (and introduced extra coupling)

**Remember**

> Refactoring is a delicate balancing act where "perfect code" does not exist. Considering the latter: don't fall into the trap of discussing 'tastes' rather than being pragmatic and shipping features.