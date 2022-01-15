
# How to use your repository (for people that don't know git)

Firstly you must have git installed as well as the git lens extension

<br>

### **Windows Link**

https://github.com/git-for-windows/git/releases/download/v2.34.1.windows.1/Git-2.34.1-64-bit.exe


<br>

### **Linux Install**

If you’re on Fedora (or any closely-related RPM-based distribution, such as RHEL or CentOS), you can use dnf:

<br>

```bash
 $ sudo dnf install git-all
```

<br>

If you’re on a Debian-based distribution, such as Ubuntu, try apt:

<br>

```bash
 $ sudo apt install git-all
```

<br>

### **Mac Os Install**

https://git-scm.com/download/mac

<br>

### **Gitlens Extension**

You can install it using the vscode marketplace

<br>

# Open a terminal in the folder you want to write code in

<br>

```shell
 git init

 git clone <link to the github repository>

```

<br>

And cd into your repository folder

<br>

# How to push your changes to the repository

<br>

First you need to stage your changes using this command

<br>

```shell

 git add .

```

<br>

Now you need to make a commit explaining the changes you made
in a few words

<br>

```shell
 git commit -m "<text>"
```

<br>

The -m allows you to add a description to the commit

<br>

now just use the git push command

<br>

```
 git push
```

<br>

# How to update your code from your github repository

If for example another person has pushed some a change to a github repository you can update the code using

<br>

```shell
 git pull
 ```

