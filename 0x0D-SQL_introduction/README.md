# SQL Introduction

This repository contains scripts to work with MySQL databases. The task focuses on basic SQL operations like listing databases, creating tables, and querying data.

## Task 0: List all databases

The script `0-list_databases.sql` is designed to list all the databases in your MySQL server. The script is executed using the `mysql` command line tool with the following syntax:

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
