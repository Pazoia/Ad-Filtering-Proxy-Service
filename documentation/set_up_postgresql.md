# Instructions to set up PostgreSQL

### **Installation**

> Before you can use PostgreSQL you need to install it. It is possible that PostgreSQL is already installed on your system.  
> To check if you have PostgreSQL installed, run the command below.

```
$ postgres -V
```

This should return the current version of PostgreSQL installed, below is an example of what should be returned.

```
postgres (PostgreSQL) 14.6 (Homebrew)
```

> If you don't have PostgreSQL, you have to install it on your system.  
> Use the command below to install PostgreSQL with [Homebrew](https://brew.sh/)

```
$  brew install postgresql
```

Once the installation is finished, run the command to check the version again.

### **Start PostgreSQL server**

> Use the command below to start the PostgreSQL server.

```
$ brew services start postgresql
```

### **Using PostgreSQL on terminal**

> To use PostgreSQL, use the command below to connect to PostgreSQL server.

```
$ psql
```

You should now be connected to the PostgreSQL server as shown below.

```
psql (14.6 (Homebrew))
Type "help" for help.

user=#
```

The link below has various commands you can perform within the PostgreSQL server.  
[PostgreSQL Cheat Sheet](https://postgrescheatsheet.com/#/databases)

### **Create database for storage of Customers and their details**

> In your `.env` file, there is an environment variable for `DB_NAME`, now we are going to create a database that matches the name set on `DB_NAME`.  
> Use the command below to create a new database.

```
user=# CREATE DATABASE < your DB_NAME >;
```

You can check all your databases by using the command below, the newly created database should be listed there.

```
user=# \l

                                  List of databases
           Name            | Owner  | Encoding | Collate | Ctype | Access privileges
---------------------------+--------+----------+---------+-------+-------------------
 your DB_NAME              | user   | UTF8     | C       | C     |
```

### You're all set now with installing PostgreSQL, starting the server and creating a database. 🚀🚀🚀

Please continue following setting up on the [README](/README.md#setting-up-postgresql) file
