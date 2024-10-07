# Refactoring and IDE Support
Because refactoring is so important all modern Integrated Developer Environments (IDEs) have refactor capabilities built-in or have plugins available. Here we will explore the refactoring capabilities of Visual Studio Code (VSCode). We assume you have the **Python** and **Pylance** plugins installed.

## Renaming functions and variables
VSCode makes renaming functions and variables extremely easy.

### Preparation
Open a new VSCode window (`File > New Window`) and open the folder `tools-example`. The example files contain multiple typos, which we want to correct.

### Rename strategy
We have to correct variable names, function names, text in comments and text in strings. For fixing typos we have two methods to our disposal:

- Rename symbol
- Find & replace

Our strategy is first to rename our functions, then our variables and lastly strings and comments.

### Rename symbol
Let's start with `rename symbol`. To show the power of this feature, turn the `printString()` function into camel casing.

Select the function name and press `F2`. This let's us rename the function over the **entire** code base. Any reference to this function will be renamed.

Let's also rename the misspelled `nam` variable.

**Limitation**
> You cannot globally rename comments. Try it.

**Warning**
> You cannot rename built-in class methods (try renaming the `Dict.strip()` method), but be aware that you *can* rename functions and methods in the standard modules. 
>
> Try renaming the `random.choices()` function and check that it is indeed changes in the random module. And change it back to its original form to prevent problems in other code that depends on the random module.

### Find & replace
With our variables and functions renamed, we can now safely rename our strings and comments. Here we have two options:

1. Use `ctrl or cmd` + `shift` + `f` to find & replace inside a single file
2. Use `ctrl or cmd` + `shift` + `h` to find & replace inside all files

Since both files contain a misspelled 'nam' in the comments, we use `ctrl or cmd` + `shift` + `h`.

**Tip**
> Never ever rename function or variable names by hand. Not only is it slower, you might also introduce typo's and thereby bugs.

## Extracting functions
Another useful feature is the `extract into` functionality.

To show how this works you need to select the code you want to convert into a function. If we look at the `process_user_data()` function than we see that this is a good candidate for refactoring. So let's refactor this function by splitting it up in multiple, smaller functions.

1. Select the code block below:

    ```python
    name = user_data['name']
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Invalid name")
    name = nam.strip().title()
    ```
2. Use `ctrl` + `shift` + `r` to extract the function

3. Rename the assigned function name `jls_extract_def` to `process_name`

Repeat the steps above for the code below the comments:

- Process age
- Process email
- Save to database (simulated)

> Congratulations: you've mastered some very basic but powerful refactoring techniques.