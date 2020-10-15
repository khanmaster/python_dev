# Title

## Timings

45 - 60 Mins

## This lesson includes

* pyodbc set up + Docker + check connection
* Cursor introduction
* what is pyodbc
* Cursor
* Rows
* While and fetchone efficiency

We will be learning how to set up and connect to an MS SQL server, spun up locally on docker. Most students would have been through the SQL week and should have a good understanding of SQL. The queries they used during those lessons will be relevant again here as it's the same Northwind DB.

## PYODBC setup 

in this lesson we will be using the ODBC driver from microsoft to connect to a docker containerised SQL instance. The installation information for the platform you are working on can be found [here](
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017).

run through the steps with the class as MS SQL will be one of the most common set ups it will be a good exercise for the students to go through.

### Docker set up

You will fnd a word document in this folder with the instructions to set up docker. If you are at this stage of the course the Docker SQL instance should already be set up and students should be aware of the Northwind DB. 

### Connection check

Once all of the previous setup has taken place use the below code to connect to the DB:

```python
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()


cursor.execute("SELECT @@version;")  
row = cursor.fetchone()
```

the response should be:

```text
('Microsoft SQL Server 2017 (RTM-CU8) (KB4338363) - 14.0.3029.16 (X64) \n\tJun 13 2018 13:35:56 \n\tCopyright (C) 2017 Microsoft Corporation\n\tDeveloper Edition (64-bit) on Linux (Ubuntu 16.04.4 LTS)', )
```

## pyodbc introduction

All if the information contained here and the information used can be found on the pyodbc git wiki [here](https://github.com/mkleehammer/pyodbc/wiki).

### What is pyodbc?

as per the git wiki pyodbc is an open source Python module that makes accessing ODBC databases simple. An ODBC driver uses the Open Database Connectivity (ODBC) interface by Microsoft that allows applications to access data in database management systems (DBMS) using SQL as a standard for accessing the data.

essentially pyodbc is an implementation of a driver that allows you to connect to pretty much any database.

### Handling the DB connection

when connecting to databases you and using a DB connection driver you will need to pass it a connection string for it to enact that connection. Connections strings are commonly structured as `server` + `database` + `userID` + `password`. As you can see in our connection that wwe have created:

```python
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()
```
we provide all of the variables and then apply those as a connection string to the `pyodbc.connection()` function and from here on this is how our connection to the database is managed.

### Cursor

A cursor itself is a control structure that allows us to control and manage rows of data from a response. In the pyodbc instance is manage our queries directly with the db.

The cursor execute methods are used to execute the call:  

```python
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()
```

as you can see above we've already set the cursor from the connection and when used to execute a query:

```python
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()


cursor.execute("SELECT @@version;")
row = cursor.fetchone()
print(row)
```

it is the cursor object itself that is the response of data. hence we're using the and setting the row object to be use the `fetchone()` method and return the first response in the cursor query executed.

we can use multiple cursor calls, we can also reduce the variable setting needed as well:

```python
import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()


cursor.execute("SELECT @@version;")
row = cursor.fetchone()
# print(row)


cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
print(cust_rows)
```

Here you can see in the last two rows we have wrapped up our call and expected output to a variable called `fetchall()` which will return all rows, of which there are 91 in Northwind and we won't be pasting then into this lesson :-)

### Rows

Row objects are returned from the cursor fetch functions and are essentially tuples i.e.:

```python
import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = docker_Northwind.cursor()

rows = cursor.execute("SELECT * FROM Products").fetchall()

for record in rows:
    print(record.UnitPrice)
```

* `rows = cursor.execute("SELECT * FROM Products").fetchall()` here we are saving all rows from the response under rows using the fetchall() option and by using a fetch option gives us the chance to use the rows methods/functions

* `for record in rows:` We are now looping through our rows using the term records as our parsing variable
    * `print(record.UnitPrice)` here we are using the functionality of rows by calling the record and then!!! and yes this is an amazing attribute YOU CAN CALL COOLUMNS AS IF YOU WOULD A FUNCTION!!! 

Run that code!!! and you should see big list of unit prices:

```text
18.0000
19.0000
10.0000
22.0000
21.3500
25.0000
30.0000
40.0000
97.0000
31.0000
21.0000
38.0000
6.0000
23.2500
15.5000
17.4500
39.0000
62.5000
9.2000
81.0000
10.0000
21.0000
9.0000
4.5000
14.0000
31.2300
43.9000
45.6000
123.7900
25.8900
12.5000
32.0000
2.5000
14.0000
18.0000
19.0000
26.0000
263.5000
18.0000
18.4000
9.6500
14.0000
46.0000
19.4500
9.5000
12.0000
9.5000
12.7500
20.0000
16.2500
53.0000
7.0000
32.8000
7.4500
24.0000
38.0000
19.5000
13.2500
55.0000
34.0000
28.5000
49.3000
43.9000
33.2500
21.0500
17.0000
14.0000
12.5000
36.0000
15.0000
21.5000
34.8000
15.0000
10.0000
7.7500
18.0000
13.0000
```
You can do all the same things here in python as you can in SQL but what we can do now is bring the wonders of python into the mic.

As cool as this is `fetchall()` is a dangerous product as it will load the entire response into memory, I mean it needs to be stored somewhere when the program is run.

### While and fetchone efficiency

As mentioned previously the danger of using `fetchall()` is that it will store an entire response to memory, with thousands of rows being returned in some instances it will swamp the memory pretty quickly.

Ideally we want loop through an iteration that allows is to call one row at a time, action it and then discard. This is where a while loop, rows and fetchcone() come together nicely.

```python
rows = cursor.execute("SELECT * FROM Products")

rows = cursor.execute("SELECT * FROM Products")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)
```

Let's step through the above:

* `while True:` here we are creating a purposeful never ending loop! although we will be managing the break statement within the loop to ensure this will not loop forever
* `record = rows.fetchone()` Here we call our fetchone() on our call and therefore only committing to one line in memory to manage at a time.
* `if record is None:` this is our all important capture statement because once we run out of records pyodbc returns none and we can the use break
    * `break` .... speaks for itself
    
This is a more efficient way of managing our DB calls.


# Next steps 

Have the students investigate the documentation on pyodbc before moving onto the structuring of functions / classes to make things a cleaner and more object orientated.

## Summary

You just:
* pyodbc set up + Docker + check connection
* Cursor introduction
* what is pyodbc
* Cursor
* Rows
* While and fetchone efficiency