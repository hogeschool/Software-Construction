# Properties of Clean Code

## What is "clean" code?
As opposed to "dirty" code, Clean Code is code that is

- Well-documented
- Well-tested
- Easy to read
- Easy to adjust
- Easy to extend

In short: Clean Code is quality code that is easy to work with.

## Examples of Clean Code
To better understand what Clean Code is, let's look at some examples. This should give us some guiding when we encounter "dirty" code that needs to be refactored.

### Well-documented
Clean Code is well-documented. The easiest way to document your code is to include the explanation inside your code with **docstrings**. Docstrings are similar to comments but with the advantage of auto-documenting your code.

**Remark**
> Docstrings describe the structure of your code (method names, parameters, ...) while comments are generally added to explain what an algorithm does or clarify the steps within a task. Comments should **not** repeat what the code already does, like 'adds 1 to the variable' for `i += 1`. In this case we can refactor our comment by just removing it. Yes, comments can also be refactored by adding some extra clarity or remove redundancy.

**Example**

```python
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def add(self, a, b):
        """
        Add two numbers.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        :return: The sum of a and b.
        :rtype: float
        """
        return a + b
```

#### Activity
Let's generate some documentation based this docstring.

To generate the documentation you could use the Sphinx module:

**Follow the Sphinx workshop**

Take a look at the `sphinx-example` folder.

### Well-tested
Clean Code is well-tested. Since refactoring is about making only **structural** changes to our code, we must be sure that its **functionality** does not change. To guarantee this we write tests. Also: if you need to refactor critical production code, you will sleep better when you have tests in place.

How to write tests will be handled in the workshop Software Testing.

### Easy to read
Clean Code is easy to read. Easy to read means that -in absence of documentation- the code explains itself. Think of propper naming of functions and variables.

**Example**

```python
def add_one(i):
    return i + 1
```

Good function names use verbs.

Besides naming, the consistency of your code base adds to its readability. That's why most teams use **code conventions**. Adhering to these conventions makes the code more predictable and thereby improves the readability.

#### Activity
- Read the article [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8) with your team
- Choose at least **two conventions** you did not yet use, but that would add the the quality of your code
- Look at the CargoHub API code and adjust some styling together
- Apply these conventions during the current coding cycle
- Reflect on its benefits after the cycle

### Easy to adjust
Clean Code is easy to adjust. Code that is easy adjust has

- No dependencies
- No coupling
- No duplication

It is of course impossible to achieve this in reality, but we should try to strive for this as much as possible.

### Activity
Looking at the CargoHub API code, what types of dependencies, coupling and duplication do you see?

**Answers**
- Use of globals
- ...
- ...

Easy to adjust code is isolated and lives in functions, modules and classes. But even if we tuck away our logic in functions, modules and classes, we cannot escape the fact that these blocks need to be glued together to form our program. How to do this properly?

#### Activity
Suppose we need to change the storage logic of our backend system. Currently we store our data in files but we need to store this data in a database. How should we do this without changing our original code too much?

**Answer**

Let's zoom out a bit.

A typical storage system can load, save, update and delete data. This is true for files and for databases. This means that we can define an **interface** to capture this behaviour:

```python
from abc import ABC, abstractmethod

class IStorage(ABC):
    """
    IStorage interface defines the basic operations for a storage system.
    """

    @abstractmethod
    def load(self, key):
        """
        Load data from storage by key.

        :param key: The key to identify the data.
        :return: The loaded data.
        """
        pass

    @abstractmethod
    def save(self, key, data):
        """
        Save data to storage.

        :param key: The key to identify the data.
        :param data: The data to save.
        """
        pass

    @abstractmethod
    def update(self, key, data):
        """
        Update existing data in storage.

        :param key: The key to identify the data.
        :param data: The new data to update.
        """
        pass

    @abstractmethod
    def delete(self, key):
        """
        Delete data from storage by key.

        :param key: The key to identify the data.
        """
        pass
```

We can now define two classes that implement this interface.

For our file key-value storage:

```python
class FileStorage(IStorage):
    def load(self, key):
        # logic to load the data to disk

    def save(self, key, data):
        # logic to save the data from disk

    def update(self, key, data):
        # logic to update the data from disk

    def delete(self, key):
        # logic to delete the data from disk
```

For our key-value database storage:

```python
class DatabaseStorage(IStorage):
    def load(self, key):
        # logic to load the data from database

    def save(self, key, data):
        # logic to save the data to database

    def update(self, key, data):
        # logic to update the data from database

    def delete(self, key):
        # logic to delete the data from database
```

In our backend logic we only need to change

```python
storage = FileStorage()
```

to

```python
storage = DatabaseStorage()
```

and the code below would still work, but with a different storage engine:

```python
storage.load(key)
storage.save(key, data)
storage.update(key, data)
storage.delete(key)
```

Interfaces also make extending easy: define the interface for a Photoshop plugin and any vendor that implements this interface can be included into Photoshop. By the way: the best **physical interface** ever designed may well be plug and holes of the power outlet system.

**Remember**

> When functions, modules and classes get in contact, use interfaces to define their coupling. It's like having a contract: it makes clear what to expect. You recognize Clean Code when the programmer applied the adagio: "Program against an interface, not against an implementation".

### Design patterns
Interfaces are part of a set of well know design patterns. When applied correctly, these patterns help us glue together our blocks of code in a maintainable manner. You can read more about design patterns in the provided resources, including how not to overdo it.

### Easy to extend
Code that is easy to adjust is also easy to extend. If we apply Object Oriented Programming (OOP) then we may extend our code via inheritence. But inheritence is also a form of coupling and, as we have seen above, this makes extending harder. Let's look at an example.

#### Activity

Going back to the example of the `Bird` class with its `fly()` method, what would be a better way to implement the `Swan` and `Ostrich` types?

**Answer**

Instead of defining a single `Bird` class and doing some weird logic bending, we could also define two bird types:

A class for the flying birds (swan, eagle, dove):
```python
class FlyingBird:
    fly(self):
        ...
```

A class for the walking birds (pinguin, kiwi, ostrich):
```python
class WalkingBird:
    walk(self):
        ...
```

By defining two distinct classes we have decoupled our logic from the `Bird` class, which makes it easier to understand and extend.

**Remark**
> We could also have zoomed out to capture the behaviour of the birds more generally in a `IMovable` interface with a `move()` method. There are many ways to tackle a problem and we just chose one here. What would be possible disadvantages of introducing a `IMovable` interface?

Note that we did change the **structure** of our code, but not its **functionality**: a swan still flies and an osterich still walks. However, it can be tricky to refactor this code safely (that's why we need tests). More on how to use refactor tools in chapter 4. Tools of this workshop.
