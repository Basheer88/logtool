# Log reporting Tool 
-----------------------
This tool will help you to print out a report (in plain text) based on the data in the database. This reporting tool is a Python program using the **psycopg2** module to connect to the database.

## Requirments
python version 2.7 ( Can be download from [here](https://www.python.org/downloads/))

psycopg2 module ( Can be download from [here](http://initd.org/psycopg/))

DataBase ( named **news** ) includes three tables:

* **Author** table includes information about the authors of articles
 ```
 name (type: text) not null
 bio (type: text)
 id (type: integer) not null default nextval('articles_id_seq'::regclass)
 ```
Indexes:
"authors_pkey" PRIMARY KEY, btree (id)

Referenced by: ( TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id) )

* **Articles** table includes the articles themselves.
 ```
 author (type: integer) not null
 title (type: text) not null
 slug (type: text) not null
 lead (type: text)
 body (type: text)
 time (type: timestamp with time zone) default now()
 id (type: integer) not null default nextval('articles_id_seq'::regclass)
 ```
Indexes:
 "articles_pkey" PRIMARY KEY, btree (id)

 "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
 
Foreign-key constraints:
 "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id) 

* **log** table includes one entry for each time a user has accessed the site
 ```
 path (type: text)
 ip (type: inet)
 method (type: text)
 status (type: text)
 time (type: timestamp with time zone) default now()
 id (type: integer) not null default nextval('articles_id_seq'::regclass)
 ```
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

## Installation
download or Clone the GitHub repository

https://github.com/Basheer88/logtool.git

# How to Get the Result
in order to execute it use your Terminal (Linux, Mac )user or GitBash for (windows) user or python idle depend on your system.

open **( logtool )** file
there is Three function inside 
* **def getTopArticles()**
 Get the Top Three most viewed Articles of all time. 
* **def getTopAuthors()**
 Get the top most viewed Authors.
* **def getError()** 
 Get all days who have more than 1% error.

# DataBase Query
inside every function in logtool file there is an sql query so if you want to do something else you need to modify that sql query to satisfy your wished. 
 ### Views
 I had created two views inside the database in postgresql so you need to create them in order to let the logtool works succesffuly  There is two views:
 ##### A1 
 ```
 create view A1 as select time::DATE, count(*) as er from log where status like '%4%' group by time::DATE order by time::DATE desc;
 ```
#### A2
```
create view A2 as select time::DATE, count(*) as total from log group by time::DATE order by time::DATE desc;
```
##### If you dont want to use views then you need to modify the sql query in ( getError() ) function in the logtool file 

# License
Free license. Feel free to do whatever you want with it.