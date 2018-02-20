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
