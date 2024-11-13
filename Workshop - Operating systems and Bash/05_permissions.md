# Permissions and Ownership
In Unix-like operating systems, managing file permissions and ownership is crucial for maintaining system security and ensuring that users have appropriate access to files and directories. Each file and directory has a set of permissions that determine who can read, write, or execute them. These permissions are divided into three categories: owner, group, and others.

## File permissions
In Unix-like systems, each file and directory has a set of permissions that determine who can read, write, or execute them. These permissions are divided into three categories:

- **Owner**: The user who owns the file.
- **Group**: The group that owns the file.
- **Others**: All other users.

Each category has three types of permissions:
- **Read (r)**: Permission to read the file or list the directory contents.
- **Write (w)**: Permission to modify the file or directory.
- **Execute (x)**: Permission to execute the file or access the directory.

You can view the permissions of a file using the **ls -l** command:
```sh
ls -l myfile.txt
```

Output:

```
-rw-r--r-- 1 user group 1234 Oct  3 14:18 myfile.txt
```

In the above example `-rw-r--r--` indicates the permissions.
* `-`: File type (dash means a regular file).
* `rw-`: Owner permissions (read and write).
* `r--`: Group permissions (read only).
* `r--`: Others permissions (read only).

### Assignment
Use `ls -l` to view the permissions of files in your home directory.

<br>

## Changing permissions
You can change the permissions of a file using the `chmod` command. There are two ways to use `chmod`: symbolic and numeric.

**Symbolic Mode**:
* `u`: User (owner)
* `g`: Group
* `o`: Others
* `a`: All (user, group, and others)

```sh
# Add execute permission for the owner
chmod u+x myfile.txt

# Remove write permission for the group
chmod g-w myfile.txt

# Set read and write permissions for all
chmod a+rw myfile.txt
```

### Assignment
Create a command that adds execute permission for the owner and removes write permission for others on a file.
> *Hint: Use `chmod u+x` and `chmod o-w`.*

<br>

**Numeric Mode**
Permissions can also be represented by numbers:
* `r` = 4
* `w` = 2
* `x` = 1

Combine these values to set permissions. For example, 7 (4+2+1) means read, write, and execute.

```sh
# Set permissions to rwxr-xr--
chmod 755 myfile.txt
```
So, the permissions in the above example are:

- **7 (Owner)**: `rwx` (4 + 2 + 1 = 7)
- **5 (Group)**: `r-x` (4 + 1 = 5)
- **5 (Others)**: `r-x` (4 + 1 = 5)

### Assignment
Permissions (Numeric Mode): Write a command that sets the permissions of a file to rwxr-xr--
> *Hint: Use `chmod 755`.*

<br>

## Ownership
Each file and directory has an owner and a group. You can change the ownership using the `chown` command.

```sh
# Change the owner to 'newuser'
chown newuser myfile.txt

# Change the owner and group
chown newuser:newgroup myfile.txt
```

### Assignment
Create a command that changes the owner of a file to a different user.
> *Hint: Use `chown newuser`.*

<br>