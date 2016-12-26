# SPJRUD to SQL

## Introduction
Learning database theory, we have been asked to write a Python program that translate SPJRUD to SQL to make requests to an SQLite database. This document describe implementation choices.

## Structure
An abstract class `Relation` is used as base for all operators. This class can be instancied but will not be able to do all operations such as `toSQL()` method. It is composed mainly of schema attributes. Subclasses of `Relation` :
- `SQLiteRelation` that gets attributes from an existing SQLite database
- all SPJRUD Operators described below

Each subclass can override `toSQL()` method to return the compiled SQL query of its representation.
SQL can then be passed to SQLite `execute()` method to get data resulting from query.

## SPJRUD Operators

### Select
There are two kinds of `Select` :
- `SelectAttribute` that returns tuples if values from two columns are equals
- `SelectConstant` that returns tuples if value from one column equals a constant

### Project
Reduce the number of attributes in the returns tuples.

### Join
Returns tuples only if corresponding values are in both subrelation1 and subrelation2.

### Rename
Rename an attribute.

### Union
Returns tuples from two relations with same attributes.

### Difference
Returns tuples in the first relation that does not appear in the second one. Both relations must have same attributes.

## Tests
To allow you to easily see all possibilities given by this application, we created a file `test.py` listing all usage of created classes and all common errors. It is obvious that you can chain object in a more complex way to make powerful requests but we let you imagination do the job.

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
According to SQLite documentation, column does not have a cast type. The type of a column is in some way informative. Only "weird" stuff happen when comparing TEXT type to other type. In this project, we decided to restrict type comparison from TEXT to other values but other values can be compared without problem (e.g. an `INTEGER` with a `FLOAT`).

## Escape attribute names and values
To avoid errors when providing quotes or spaces within attribute names and values, it is required to escape them.
According to [this page](https://www.sqlite.org/lang_keywords.html), attribute names can be escaped with double quotes as `"attr_name"` and attribute values can be escaped with single quotes `'attr_value'`. This is the way attribute names and values are escaped in this project before inserting them into SQL query.
