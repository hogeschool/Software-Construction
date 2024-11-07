# Shell scripting
Shell scripting is a powerful way to automate tasks and manage system operations in Unix-like operating systems. A shell script is essentially a text file containing a sequence of commands that the shell interprets and executes. These scripts can perform a wide range of tasks, from simple file manipulations to complex system administration tasks.

Shell scripting is particularly useful for:
- **Automating repetitive tasks**: Scripts can save time by automating routine operations.
- **Batch processing**: Execute a series of commands on multiple files or directories.
- **System administration**: Manage system configurations, backups, and other administrative tasks.
- **Customizing environments**: Set up user environments and preferences.

<br>

## Creating
To create a shell script, you simply need to create a file with the a command. \
For example, you can use `touch`, `nano` or `vim` to create a file named `myscript.sh`

```sh
touch myscript.sh
```
<br>

## Shebang
The shebang (`#!/bin/bash`) is the first line in a script that tells the system which interpreter to use to execute the script.
```sh
#!/bin/bash
# This is a comment
echo "Hello, World!"
```

## Running
Running your script is as easy as calling it inside the terminal: `./myscript.sh` \
But before we can do this, we need to make it executable first:
```sh
chmod +x myscript.sh
```
> :information_source: You only need to make the script executable once.


### Assignment
Write a script that prints “`Hello, World!`” to the console.
> *Hint: Use echo to print text.*

<br>

## Variables
Bash has the option to set and use variables just like other programming langueges.

**Setting variables** \
You can set variables in a shell script by simply assigning a value to a name.
```sh
#!/bin/bash
name="John"
```

<br>

**Using variables** \
To use a variable, you prefix it with a `$`
```sh
#!/bin/bash
name="John"
echo "Hello, $name!"
```

### Assignment
Modify the script to use a variable for the name and print “`Hello, [name]!`”
> *Hint: Set a variable and use it with echo.*

<br>

## Conditionals
Bash also has some conditionals you can use. `if`, `elif` and `else` allow you to execute different codes based on certain conditions.

```sh
#!/bin/bash
number=10

if [ $number -gt 5 ]; then
  echo "The number is greater than 5"
elif [ $number -eq 5 ]; then
  echo "The number is equal to 5"
else
  echo "The number is less than 5"
fi
```


**Exit status (`$?`)**
The exit status of the last command executed is stored in the `$?` variable.

```sh
#!/bin/bash
ls /nonexistent_directory
if [ $? -ne 0 ]; then
  echo "The last command failed"
fi
```

### Assignment
Write a script that checks if a number is `positive`, `negative`, or `zero`.
> *Hint: Use `if`, `elif`, and `else` to check the number.*

<br>

## Loops
Just like Python, Bash also has some loops available to use.

**For-loops** \
For-loops allow you to iterate over a list of items.
```sh
#!/bin/bash
for i in 1 2 3 4 5; do
  echo "Number: $i"
done
```
This loop will print numbers from 1 to 5 based on the range `1 2 3 4 5`.\
The `{1..5}` syntax generates a sequence of numbers.

<br>

You can also use for-loops to iterate over arrays:
```sh
#!/bin/bash
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
  echo "Fruit: $fruit"
done
```
This loop will print each fruit in the array.

<br>

**While-loops** \
While-loops continue to execute as long as a condition is true.
```sh
#!/bin/bash
counter=1
while [ $counter -le 5 ]; do
  echo "Counter: $counter"
  ((counter++))
done
```
This loop will print the counter value from 1 to 5. The ((counter++)) syntax increments the counter.

<br>

Just like Python you can also create an infinite While-Loop.
> :warning: *Be cautious with conditions to avoid infinite loops*

```sh
#!/bin/bash
while true; do
  echo "This will run forever. Press Ctrl+C to stop."
done
```

### Assignment
Create a script that prints numbers from 1 to 10 using a `for-loop` and a `while-loop`.
> *Hint: Use `{1..10}` for the for-loop and a `counter` for the while-loop.* 


<br>

## User input
Sometimes we want to run the script, but leave some options open to the input of the user. \
For this you can use the `read` command to get input from the user:

```sh
#!/bin/bash
echo "Enter your name:"
read name
echo "Hello, $name!"
```

<br>

## Functions
Functions group code into reusable blocks. They can take arguments and return values.

**Defining Functions**
We can define a function by using `<function_name>(*args) { ... }`.

```sh
#!/bin/bash
greet() {
  local name=$1
  echo "Hello, $name!"
}
```

Using `local` helps avoid unintended side effects by ensuring that variables within functions do not affect or get affected by variables outside the function

```sh
#!/bin/bash

# Global variable
name="Alice"

greet() {
  # Local variable
  local name="Bob"
  echo "Hello, $name!"
}

echo "Global name: $name"
greet
echo "Global name after function call: $name"
```

Will output:
```
Global name: Alice
Hello, Bob!
Global name after function call: Alice
```


<br>

**Using Functions**
Call a function by its name and pass arguments if needed.

```sh
#!/bin/bash
greet() {
  local name=$1
  echo "Hello, $name!"
}

greet "Alice"
```

### Assignment
Write a script with a function that takes a name as an argument and prints a greeting.
> *Define a function and call it with an argument.* 


<br>

## Handling Parameters
Scripts can accept arguments from the command line. \
These are accessed using positional parameters `$1`, `$2`, etc.

```sh
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
```

You can run this script with arguments like so:
```sh
./myscript.sh arg1 arg2
```

<br>

**Special Parameters**
* `$#`: Number of arguments
* `$@`: All arguments as a list
* `$*`: All arguments as a single string
* `$0`: The name of the script

```sh
#!/bin/bash
echo "Script name: $0"
echo "Number of arguments: $#"
echo "All arguments: $@"
```

### Assignment
Modify the script so we can enter our name as an argument when running the script: `./myscript.sh John`, \
should output `Hello, John!`

<br>