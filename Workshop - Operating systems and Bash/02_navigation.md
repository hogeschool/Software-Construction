# Navigating the File system 
Navigating the filesystem via the shell is a fundamental skill for anyone using an operating system, especially for tasks involving system administration, development, or automation. \
Mastering these commands will make you more efficient and capable of performing a wide range of tasks. 


## Working directory
Let's start by checking out our working directory

    $ pwd

will give us the current directory we are in, depending on your operating system the output can vary. \
*What did your `pwd` show?*

<br>

## List files and directories
When we are in a directory we can list all files and directories in that directory by using: 

    $ ls


This will print a list of all files and directories, *can you see the difference in the output?*

    Stuff/
    Downloads/
    favorite_characters.png
    requirements.docx

Sometimes we only want to see more information about files and directories, for this you can use `flags`.
> If you ever forget the flag of a command, use `--help` to generate a list of helpful flgas.

    $ ls -a

Will generate a list of all files and directories (including hidden):

    ./
    ../
    .hiddenfile
    Stuff/
    Downloads/
    favorite_characters.png
    requirements.docx


    $ ls -l

Will generate a list of all files and directories with additional information about permissions, filesize, last update

    drwxr-xr-x  2   user user   4096    Sep 12 12:00    Stuff/
    drwxr-xr-x  2   user user   4096    Sep 12 12:00    Downloads/
    -rw-r--r--  1   user user   123     Sep 12 12:00    favorite_characters.png
    -rw-r--r--  1   user user   123     Sep 12 12:00    requirements.docx

> You can combine flags to get more or less information when using commands, `ls -al` will give all information including hidden files.

<br>

## Changing directory
In many situations we want to change the directory we are currently in, to either view the files inside that directory or do other things like creating, moving or copying something to or from it. For those situations we need to **change directories**.

    $ cd

Is the command you can use to provide this *changing* service. It stands for **c**hanging **d**irectory. \
`cd` on it's own won't do much, we need to add the desired directory we want to go to behind it.

    $ cd Stuff

Our working directory has also changed when using `cd`

    $ pwd
    /home/user/Stuff

Will bring us inside the `Stuff/` directory we saw in the list from `ls` earlier. \
Going up a single directory can be achieved via `../`, so:

    $ cd ../

Checking the current working directory (the directory we are in)

    $ pwd
    /home/user


Will reveal that we moved up **one** directory.
> If you want to move up multiple directories you can just add more `../` after each other, `../../` will move up **two** directories.

Sometimes we want to get *home*, this can be achieved by using `~` which is a shortcut alias for the home directory of the current user.

    $ cd ~

    $ pwd
    /home/user


<br>

## Filtering
Filtering is a powerful technique in shell scripting and command-line usage, allowing you to search for and manipulate data efficiently. Two commonly used commands for filtering are `find` and `grep`.

<br>

### Using `find`
The `find` command is used to search for files and directories within a directory hierachy based on various criteria.

**Basic syntax**

    find [path] [expression]


Let's see if we can find all files in our current folder

    $ find . -type f -name "*.docx"
    ./requirements.docx
    ./Downloads/template.docx
    ./Stuff/Informatica/skills.docx
    ./Stuff/Informatica/slc.docx

Giving the `-type f` flag to `find` will search for the type `file`.
> Can you figure out the flag for directories only?

`-name "*.docx"` is an extra flag in our search, besides only files, we also only want `.docx` files. \
Giving the `-name` flag will give you the option to search for specific names the `*` *(wildcard)* in the name followed by the extension searches only for everything, extension `.docx` in this example.
> Can you figure out the flag for all files containing the word `school` in it?

<br>

There are even more flags to discover, do some research about extra flags for `find` and discuss where they could be used for. 

> Could you figure out what the following commands would do?

    $ find . -size +100M


    $ find . -mtime -7


    $ find . -name "*.log" -exec rm {} \;


<br>


### Using `grep`
The `grep` command is used to search for patterns within files. It stands for "Global Regular Expression Print".

**Basic syntax**

    grep [options] pattern [file...]

> More about `grep` later on in this workshop

<br>

### Combining
You can combine `ls` and `grep` to perform filtering on `ls`. \
For example, to display only files:

    $ ls -p | grep -v / 