# Git Basics

* `git log -10` - Show the last ten commits
* `git diff --stat <hash_num>` - Prints stats about changes made since the commit specfied.
* `git revert <hash_num>` - Rolls back changes made to the commit specified with a new commit. ALWAYS REVERT TO THE MOST RECENT COMMIT.
  * `-n` - A flag used when you want to revert multiple commits. It allows you git rever multiple times without commiting
    until you are ready.
* `git reset <hash_num> --hard` - Resets an entire repository back to a previous commit. (THIS CANNOT BE UNDONE)
* `git reset <hash_num> <filename> --hard` - Resets a particular file back to a previous commit. (THIS CANNOT BE UNDONE)

## States

Git has three main states that your files can reside in: committed, modified, and staged.

* __Modified__: You have changed the file in your Working Directory but have not added it yet.
* __Staged__: You have marked a modified file to go into the Staging Area for your next commit.
* __Committed__: Data is safely stored from the Staging Area into your local .git Directory.
  * Working Directory: A single checkout of the project. These files are pulled out of the compressed database in the Git Directory and placed on disk for you to use or modify.
  * Staging Area: Is a simple file, generally contained in your Git directory, that stores information about what will go into your next commit -- basically an "index" of the staged files.
  * Git Directory (Repository): Metadata & Object Database of the project (a compressed reference "skeleton" of the project). This is the essential part of Git -- it's what is copied when you clone a repository from GitHub or another computer.

## Github Repo Link 

`git remote add origin https://github.com/<github username>/<github repo name>.git`

## Merging

* `git merge --squash <branch to merge>` - takes all the history of one branch and compresses it into one commit in the other branch. These are helpful when you’re creating a  new feature or fixing a bug that requires some experimentation. You don’t need each commit tracing your experiments; you just need the final outcome.
* `git merge --abort` - Aborts a merge (ALWAYS COMMIT ALL CHANGES BEFORE ATTEMPTING A MERGE.)

## Fetching

If you forked before cloning, to keep track of the original repository, you need to add another remote repository named upstream that points to the original. You will use the upstream remote to fetch the changes made to the original repository since you forked it. If you want to send your changes to the original repository, you need to submit a pull request from your GitHub repository.

When fetching from your GitHub repository:

`$ git fetch origin master`

When fetching from the original GitHub repository:

`$ git fetch upstream master`

Also, note that fetch needs to be followed by a merge!

Or, you can use the pull command which is a shortcut for fetch + merge.

`$ git pull origin master -m "this is a fetch and a merge in one command!"`