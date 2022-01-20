<h1 align="center">
  <strong>Template - Gilmore Gigabytes</strong>
</h1>

<br>

<h3 align="center">
  <a href="#">Contributions</a>
  <span>·</span>
  <a href="https://github.com/GilmoreGigabytes/Template/blob/main/documentation/files/documentation.md">Documentation</a>
</h3>

---

<br>

## **Disclaimer**

### Most, if not all of this code will not run if you are not using the Spike Prime extension for Visual Studio Code <a href="https://marketplace.visualstudio.com/items?itemName=PeterStaev.lego-spikeprime-mindstorms-vscode" target="_blank">Download here</a>, and make sure to use python 3.10.1 when uploading your code to the Spike Prime.

<br>

## How to PR this virtual repository and create commits:
1. To get started with interacting with this repository from your PC, we suggest that you install GIT. If you're on a Linux-based OS such as Arch or MacOS, this does not apply to you. Although, if you have unintalled GIT before, you will have to reinstall it using the command: `sudo apt update && sudo apt upgrade && sudo apt install git` in your terminal (`sudo` being optional. Although advised to not use `root` login for security). For non-linux-based OS' you can follow <a href="https://git-scm.com/downloads" target="_blank">this</a> download link and install directly from there.
2. Optionally you can also install the <a href="https://desktop.github.com/" target="_blank">GitHub desktop client</a> so that you can make PRs and Commits without the CLI (command-line), especially if new to this as you can severely screw up your PC if you type the wrong command or if you do not know what you're doing.

For this portion of the tutorial we will be using the CLI (command-line) as it is recomended. If you need help with the Github Desktop client, you may search around on their website or your search engine of choice.

3. Firstly find the repository that you would like to contribute to.
4. Now we must clone our repository GIT web url. The image below demonstrates how you may do that:
![There are numbers under each arrow, follow them in order. For each step click with your left mouse button.](https://media.discordapp.net/attachments/879991970167160832/931775304626753586/Screen_Shot_2022-01-15_at_12.57.31_pm.png?width=1008&height=572)
5. You'll have to change directories to your desktop. open Terminal on a linux-based OS or PowerShell (in administrative mode) on a Windows OS, then run `cd <PATH_TO_WORKSPACE>`. Replacing <PATH_TO_WORKSPACE> with the path to the directory you want to store the repoistory in. On Linux-based OS' such as MacOS it would look something like: `~/Desktop` whilst on Windows OS' it would look something like `C:\Users\<USERNAME>\Desktop\`. Remember to change <USERNAME> to **your** username.

9. Once you've made your changes and are ready to pull you can reopen your Terminal or Powershell and change directories into the local repository using the `cd` command.
10. Now you can start to push your changes to the virtual repository, let's begin shall we? Firstly, run `git add .` whilst inside of your local respository in the command-line. This adds all your local changes to a commit.
11. Once done, you can set a commit message to tell people what you did, you can do this by running `git commit -m "<COMMIT_MESSAGE>"`, replacing <COMMIT_MESSAGE> with your message. Please note, not all special characters (symbols) are allowed in the commit message, so if it fails and says something about characters, you know what to do.
12. Now that we have set our commit message we may proceed to pushing to the virtual repository. You can do this by running `git push` (P.s. When running `git push`, `git pull` or `git merge` you may be prompted to login, if yes, grab that Personal Access Token which you saved and paste it in for the username then click enter and also paste it in for the password and click enter. If you run this and you get an error about changes on the Github repository that you do not have locally, run: `git merge`. **BEWARE**, your changes **COULD BE OVERWRITTEN!**, depending on if the changes on the virtual repository edit stuff which **you edited**. After running git merge, go back to your code and check to see if anything was overwritten, if it was, change it again and then repeat steps #10, #11 and #12.
13. Now verify that your stuff was pushed by heading over to the virtual repository. It will say that you recently pushed.

  
  
## How to pull latest changes off of virtual repository:
1. Open Terminal if on a Linux-based OS or administrative PowerShell if on a Windows OS.
2. Now we must change directories into your local respository,`cd <PATH_TO_LOCAL_RESPOSITORY>`, replacing <PATH_TO_LOCAL_RESPOSITORY> with the path to your local respository. You learnt how to find it in the `How to PR this repository and create commits:` tutorial.
3. Run: `git pull` to pull changes from virtual respository and you're done.
  
  

## Documentation for Judges
### Windows
In this repository there is a PowerShell script that will take all of your commit history and dump it into a file called judgeDocumentation.md. Make sure that you do this on the day of your competition.
### Linux
In this repository there is a BASH script that will take all of your commit history and dump it into a file called documentation.md. 

*Running the script a second time will result in the documentation.md file being overwritten, so don't worry about deleting it. Just make sure it's up-to-date.*
  
 <br>
  
 ### This Readme was written by <a href="https://github.com/Bytedefined" target="_blank">**Bytedefined**</a>

 <br>
