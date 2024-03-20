# Shell Basics

This folder contains scripts that demonstrate various concepts and commands related to shell scripting.

## Scripts:

### 0-current_working_directory
Prints the absolute path name of the current working directory.

### 1-listit
Displays the contents list of the current directory.

### 2-bring_me_home
Changes the working directory to the user's home directory.

### 3-listfiles
Displays the current directory contents in a long format.

### 4-listmorefiles
Displays the current directory contents, including hidden files, in a long format.

### 5-listfilesdigitonly
Displays the current directory contents in a long format, with user and group IDs displayed numerically, including hidden files.

### 6-firstdirectory
Creates a directory named "my_first_directory" in the `/tmp/` directory.

### 7-movethatfile
Moves the file "betty" from `/tmp/` to `/tmp/my_first_directory/`.

### 8-firstdelete
Deletes the file "betty" from `/tmp/my_first_directory/`.

### 9-firstdirdeletion
Deletes the directory "my_first_directory" from the `/tmp/` directory.

### 10-back
Changes the working directory to the previous one.

### 11-lists
Lists all files in the current directory, the parent of the working directory, and the `/boot` directory, in long format.

### 12-file_type
Prints the type of the file named "iamafile" in the `/tmp/` directory.

### 13-symbolic_link
Creates a symbolic link named "__ls__" to `/bin/ls` in the current working directory.

### 14-copy_html
Copies all HTML files from the current working directory to the parent of the working directory, only if they don't exist in the parent directory or are newer than the versions in the parent directory.

## Requirements

- All scripts are tested on Ubuntu 20.04 LTS.
- Each script is exactly two lines long.
- All files end with a new line.
- The first line of each script is `#!/bin/bash`.
- Backticks, `&&`, `||`, and `;` are not used.
- All scripts are executable.

Feel free to explore and run these scripts to learn more about shell scripting!

