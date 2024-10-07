# Spinx documentation
Here you find the steps to generate documentation from the docstring in the code.

## Prerequisites

### Install Sphinx
`pip install sphinx`

## Setup
We have already setup the config to speed up the workshop. If you want to do it yourself you must run `sphinx-quickstart` first and then consult the resources for some tutorials.

## Generation

### 1. Enter the project folder
`cd sphinx-example`

### 2. Check the Calculator docstrings
Open the `Calculator` class and see how we have added the docstring.

## 3. Generate the documentation
- Make sure you are in the root of the `sphinx-example` folder
- Now run `sphinx-apidoc -o ./docs ./src/` to generate the docs

## 4. View the documentation
Find the index.html and open it in your browser.

## 5. Extend the documentation
- Play around in the Calculator class, add some new methods
- Add a new module or class and see what it does to your docs

## 6. Apply to CargoHub API
Use the `sphinx-example` as a template for your CargoHub API code and start documenting your code base.