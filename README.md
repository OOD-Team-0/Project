# OOD Project Fall 2018 

## Team 0 Members:

* Dimitrios Topalis
* John Donahue
* Joseph Dementri
* Joshua Geller
* Matthew Finnegan

## How to Setup IntelliJ with this GitHub Project

1. Install IntelliJ (should be able to download professional edition with student email)
2. Have Java SDK (1.8 preferred) downloaded and in a known place, configure with IntelliJ
3. In IntelliJ's welcome screen, click `Check out from Version Control` then `Git`
4. If you haven't already, IntelliJ might make you ask which service to sign in to. Choose GitHub then sign in using your username and password.
5. After signing in, you should be presented with a dialog asking for URL and Directory. The directory doesn't matter too much, that's where the program will be stored locally on your machine. For the URL choice, you should have a drop down, in it one option should say `https://github.com/OOD-Team-0/Project.git`. That is this project. Click Clone.

You should now have the project cloned locally to your machine

# The same as above applies to PyCharm, except you choose Python instead of Java SDK

## How to Setup on Command Line (for other Editors)

1. Make a new folders somewhere you can remember. Ex: `C:\Users\Joe Dementri\Desktop\OOD-Python`
2. Enter that folder. Type `git clone https://github.com/OOD-Team-0/Project.git`
3. Your project will be cloned into that folder, under a folder called Project
4. To switch to your desired branch, type `git checkout (NAME_OF_BRANCH)`
5. Open in your Git compatable editor, and enjoy.

## Working Git from the Command Line

1. Navigate back to project source folder. Ex: `C:\Users\Joe Dementri\Desktop\OOD-Python\Project`
2. Type `git add .` to stage all the files.
3. Type `git commit -m "MESSAGE GOES HERE"` to commit locally with your message.
4. Type `git push origin (NAME_OF_BRANCH)` to commit to the branch on GitHub.

If there is an error, its probably because you need to pull the changes before you can push.

5. Type `git pull origin (NAME_OF_BRANCH)` to pull the latest changes