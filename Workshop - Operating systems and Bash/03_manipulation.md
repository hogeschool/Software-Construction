# File and Directory manipulation
File and directory manipulation is a fundamental skill for anyone working with computers, especially in Unix-like operating systems. \
It involves using shell commands to create, modify, move, and delete files and directories. These operations are essential for organizing data, automating tasks, and managing system resources efficiently.

## Files
**Files** are the basic units of storage, containing data such as text, images, or executable programs.

### Creating files
To create a file we use the command: `touch [file...]` \
If we want to create a file name `readme.md` we would do the following:
```sh
touch readme.md
```

<br>

### Copying files
Copying files from one to another location can be done via the `cp [source] [destination]` command. \
The readme (although empty) is needed in another folder `src` as well, this can be done via:
```sh
cp readme.md ./src/readme.md
```

<br>

### Moving or renaming files
Sometimes we want to move or rename files, this can be managed by the same command: `mv [source] [destination]` \
The copied `readme.md` inside `src/` was needed inside `api/` not `src/`, if we want to move it we use:
```sh
mv ./src/readme.md ./api/readme.md
```

After moving it to `api/` we found out it should be called `endpoints.md` to describe all the endpoints this api will cover, we can rename this file by using:
```sh
mv ./api/readme.md ./api/endpoints.md
```
> If you want to forcefully move a file to overwrite an existing file (by default there is a comfirmation), you can use the `-f` flag. \
> If you want to move all files to folder but don't want to overwrite existing files, you can use the `-n` flag.

<br>

### Deleting files
Getting rid of a file is easy by just deleting it, the command: `rm [file...]` does just that. 
> :warning: *In linux, removing an item (or directory) is a permenant operation!*
 
During our development we found out that someone also uploaded a very detailed `endpoints.yml`, so we can get rid of our just created `endpoints.md` by doing the following:
```sh
rm ./api/endpoints.md
```
> If you want a confirmation before deleting, just add the `-i` flag to the command `rm -i [file...]` \
> If you want to forcefully remove a file, you can use the `-f` flag.

<br>

### Assignment
1. Create a file named `assignment.txt`
2. Copy this file to a new file called `solution.txt`
3. Rename `assignment.txt` to `assignment.md`
4. Delete the `solution.txt` file

<details markdown="1">
<summary align="right">Show solution</summary>

```sh
touch assignment.txt
cp assignment.txt solution.txt
mv assignment.txt assignment.md
rm solution.txt
```
</details>

<br><br>

## Directories
**Directories** (or folders) are containers that hold files and other directories, helping to organize the file system in a hierarchical structure.

### Creating a directory
If we want to create a new directory you can use the `mkdir [name]` command. \
Let's say we want to have some tests later in our current working folder we can do:
```sh
mkdir tests
```

<br>

### Copying a directory
Copying a directory from one location to another can be done via the `cp -r [source] [destination]` command.
> :information_source: `-r / -R / --recursive` is the flag for copying recursively. \
> *When you copy directories recursively, it means that you copy not just the directory itself, but also all of its contents, including subdirectories and their contents, and so on. Essentially, it’s like copying the entire tree structure of the directory.*


We already have some tests available that we want to put inside our just created `tests` folder, you can use:
```sh
cp -r unit tests/
cp -r intgration tests/
```

> *If you want to keep all file characteristics (modification time, access time, etc) you can use `-p` as an extra flag.*

<br>

### Moving or renaming a directory
Moving or renaming an directory is the same as with a file, we use the `mv [source] [destination]` command for that. \
We accidently named one of our folders incorrect `intgration` vs `integration`, we could fix this by doing:
```sh
mv tests/intgration tests/integration
```
> If you want to forcefully move a folder over an existing folder (by default there is a comfirmation), you can use the `-f` flag.


<br>

### Deleting a directory
To remove a directory we have two options, you can use `rmdir` if our directory is empty, \
or `rm` to remove complete directories, including subdirectories and files.

> :warning: *In linux, removing a directory (or item) is a permenant operation!*

Let's say we have two directories called `stuff` and `empty` that we want to get rid of, we ca use:
```sh
rm -r stuff
rmdir empty
```

<br>

### Assignment
1. Create a directory called `workshop`
2. Inside this directory create two files `assignment.md` and `solution.md`
3. Copy `solution.md` to a new file called `alternative.md`
4. Create a new directory called `solutions`
5. Move both `solution.md` and `alternative.md` inside this new directory
6. Make a copy of the `solutions` directory and call it `alternatives`
8. Remove the `alternative.md` file from the `alternatives` folder
9. Delete the `alternatives` folder including all remaining files

<details markdown="1">
<summary align="right">Show solution</summary>

```sh
mkdir workshop
touch assignment.md solution.md
cp solution.md alternative.md
mkdir solutions
mv solution.md alternative.md solutions/
cp -r solutions alternatives
rm alternatives/alternative.md
rm -r alternatives
```
</details>

<br>