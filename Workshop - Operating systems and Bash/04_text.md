# Text processing with Bash
Text processing is a crucial aspect of working with data in Unix-like operating systems. \
Bash, provides a powerful set of tools and commands for manipulating and analyzing text files. \
These tools enable users to perform a wide range of tasks, from simple text searches to complex data transformations.

Text processing involves operations such as searching, filtering, transforming, and extracting data from text files. \
Common tasks include finding specific patterns, replacing text, sorting lines, and summarizing data. \
Bash commands like `grep`, `sed`, `awk`, `cut`, and `sort` are essential for these operations.

## Viewing File Content
Viewing the content of files is a fundamental task in text processing.

<br>

### Displaying and Concatenation

To display file contents or to concatenate several files, we can use `cat [files...]`.
```sh
cat filename.txt
```

<br>

### More or Less

Sometimes we don't want all the information at once, but want it in pieces (page by page).\
We can use `less [file]` and `more [file]` to get less and/or more of the information.

```sh
less filename.txt
```

<br>

### Head & Tail

Viewing the complete file or even page by page is not always ideal if you just want to check some parts.\
If you want to check if some information is present in the top of a file, we can use `head -n [number_of_lines] [file]`.

```sh
head -n 10 filename.txt
```

Let's say you want to check if a log file has some line added to it (normallya added to the end of the file). \
To see the end of a file, we can use `tail -n [number_of_lines] [file]`.

```sh
tail -n 10 filename.txt
```

<br>

### Exercises
1. Use cat to display the content of a file named example.txt.
2. Use less to view the same file and navigate through it.
3. Display the first 5 lines of example.txt using head.
4. Display the last 5 lines of example.txt using tail.

<br>

## Searching

In a previous chapter you have learned that `find` is the command to search for files in directories.

    find /path/to/directory -name "filename.txt"

<br>

### Comprehensive search

The `grep` command is used to search for patterns within files. It stands for "Global Regular Expression Print".


    grep [options] pattern [file...]

<br>

If you need to search for some specific information, and want to make sure if it's present in a file.

    $ grep "Als een gebruiker" requirements.docx
    Als een gebruiker wil ik kunnen inloggen met een email and wachtwoord

<br>

Sometimes you want to perform this search, but case-insensitive.

    $ grep -i "Als een gebruiker" requirements.docx
    Als een gebruiker wil ik kunnen inloggen met een email and wachtwoord
    als een gebruiker wil ik mijn email kunnen wijzigen

<br>

If the file is very big, it might be handy to show what linenumber these sentences are on, this can be managed by adding the flag `-n`

    $ grep -n "Als een gebruiker" requirements.docx
    4:Als een gebruiker wil ik kunnen inloggen met een email and wachtwoord

### Research
Could you figure out what the following flags in combination with the command would do?

    $ grep -r "search_term" /path/to/search


    $ grep -c "serach_term" filename.txt


    $ grep -v "search_term" filename.txt

### Exercises
1. Use `grep` to find the term “Bash” in `example.txt`.
2. Use `grep` with the -i option to perform a case-insensitive search for “bash” in `example.txt`.
3. Use `find` to locate a file named `example.txt` in your home directory.

<br>


<br>

## Redirecting Input/Output
Redirecting input and output allows you to control where the data goes. 

<br>

### Redirecting output

The `>` operator redirects the output of a command to a file, overwriting the file if it already exists.

    echo "Hello, World!" > output.txt

> This command writes “Hello, World!” to `output.txt`. If `output.txt` already exists, its content will be replaced.

<br>

### Appending output

The `>>` operator redirects the output of a command to a file, appending to the file if it already exists.

    echo "Hello again!" >> output.txt

> This command adds “Hello again!” to the end of `output.txt` without removing the existing content.

<br>

### Redirecting input

The `<` operator redirects input from a file to a command.

    sort < unsorted.txt

> This command sorts the content of `unsorted.txt` and displays the sorted output.

<br>

### Piping
The `|` operator, known as a pipe, takes the output of one command and uses it as the input for another command.

    cat filename.txt | grep "search_term"

> This command displays the content of `filename.txt` and then searches for “search_term” within that content.

<br>

### Combinations

You can combine these operators to perform more complex tasks.

    grep "search_term" filename.txt | sort > sorted_results.txt

> This command searches for “search_term” in `filename.txt`, sorts the results, and writes them to `sorted_results.txt`.

<br>

### Error redirection

Bash also allows you to redirect error messages using `2>` for overwriting and `2>>` for appending.

    ls non_existent_file 2> error_log.txt

> This command attempts to list a non-existent file and redirects the error message to `error_log.txt`.

You can redirect both standard output and standard error to the same file using `&>` for overwriting and `&>>` for appending.

    command &> output_and_error.txt

> This command runs `command` and redirects both its output and error messages to `output_and_error.txt`.

<br>

### Exercises
1. Redirect the output of `ls` to a file named `files.txt`.
2. Append the output of `date` to `files.txt`.
3. Use `sort` to sort the contents of `files.txt` and display the result.
4. Pipe the output of `cat example.txt` to `grep` "Bash".

<br><br>

## Assignment
Combine all the skills you’ve learned in the following exercise:

1. Create a file named `workshop.txt` and add some text to it.
2. View the content of `workshop.txt` using cat.
3. Search for a specific term in `workshop.txt` using `grep`.
4. Redirect the output of the search to a new file named `search_results.txt`.
5. Append the current date and time to `search_results.txt`.
6. Use `less` to view `search_results.txt`.