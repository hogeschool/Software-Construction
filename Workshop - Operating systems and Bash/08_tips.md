# Best practices and Tips

You've learned a lot of commands during this workshop, commands designed for the shell and commands to use in Bash scripting. \
This page gives a brief overview of best practices and tips for using the shell and Bash.

<br>

### Use Tab Completion
Tab completion helps you quickly complete commands, file names, and directory names. \
Just start typing and press `Tab` to auto-complete or see suggestions.

### Command History
Use the up and down arrow keys to scroll through your command history. \
This saves time by allowing you to reuse previous commands.

Use `Ctrl + R` to search through your command history. \
Start typing a part of the command and it will show the most recent match.

### Aliases
Create aliases for frequently used commands to save time.

    alias ll='ls -la'

Add this to your `.bashrc` or `.bash_profile` to make it permanent.

### Use Wildcards
Wildcards can help you work with multiple files at once.
- `*` matches any number of characters.
- `?` matches a single character. 
- `[abc]` matches any one of the characters inside the brackets.

### Use man and --help
Use the man command to read the manual pages for commands.

    man ls

Most commands also support `--help` to display a summary of options.

    ls --help

### Redirecting Output
Redirect standard output and error to different files.

    command > output.txt 2> error.txt

### Background Processes
Run commands in the background by appending `&` at the end.

    long_running_command &

<br>

## Bash Scripting


### Start with a Shebang
Always start your script with a shebang to specify the interpreter.
```sh
#!/bin/bash
```

### Make Scripts Executable
Make your script executable using chmod.

    chmod +x script.sh

### Use Comments
Use comments to explain your code. This makes it easier to understand and maintain.
```sh
# This is a comment
echo "Hello, World!"
```

### Use Variables
Use variables to store and reuse values.
```sh
name="Alice"
echo "Hello, $name"
```

### Use Functions
Use functions to organize your code and avoid repetition.
```sh
greet() {
  echo "Hello, $1"
}
greet "Alice"
```

### Error Handling
Check the exit status of commands to handle errors.
```sh
if [ $? -ne 0 ]; then
  echo "An error occurred"
fi
```

### Use set Options
Use set options to improve script robustness.
```sh
set -e: Exit immediately if a command exits with a non-zero status.
set -u: Treat unset variables as an error.
set -o pipefail: Return the exit status of the last command in the pipeline that failed.
set -euo pipefail
```

### Use read for User Input
Use read to get input from the user.
```sh
read -p "Enter your name: " name
echo "Hello, $name"
```

### Debugging
Use `bash -x script.sh` to run your script in debug mode and see each command executed.

### Use trap for Cleanup
Use `trap` to execute commands when the script exits, which is useful for cleanup tasks.

    trap 'echo "Cleaning up..."; rm -f temp_file' EXIT