# SPJRUD to SQL

## Introduction
Learning database theory, we have been asked to write a Python program that translate SPJRUD to SQL to make requests to an SQLite database. This document describe implementation choices.

## SPJRUD
### Select
### Project
### Join
### Rename
### Union
### Difference

## Attribute types
According to [this page](https://www.sqlite.org/datatype3.html), valid SQLite types are :
- TEXT
- NUMERIC
- INTEGER
- REAL
- BLOB
Though, the SQLite command to describe a table `PRAGMA TABLE_INFO()` return one more type :
- FLOAT
To avoid false positive during type verification, we accepted types from both sources in this project.

## Attribute comparison
TODO
numeric can be compared with numeric so only text cannot be compared with other

## Escape attribute names and values
To avoid errors when providing quotes or spaces within attribute names and values, it is required to escape them.
According to [this page](https://www.sqlite.org/lang_keywords.html), attribute names can be escaped with double quotes as `"attr_name"` and attribute values can be escaped with single quotes `'attr_value'`. This is the way attribute names and values are escaped before inserting them into SQL query.
