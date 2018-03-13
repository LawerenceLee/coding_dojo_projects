# Working with mySQL

## Installation

* Use homebrew to install MySQL.
  * `brew install mysql`
* Use homebrew to start your MySQL Server as a  "service", meaning it will run in the background and allow connections.
  * `brew services start mysql`
* Now with MySQL installed, you have access to some new command line tools. Run the following command to set the MySQL root user's password to "root".
  * `mysqladmin -u root password "root"`
  * `mysql -u root -p`

## Startup Instructions

* `$ brew services start mysql`
* Open MySQL Workbench, Click on local instance. 
* Type in password of `root`
* Use: `brew services stop mysql` to stop running MySQL locally on your machine.