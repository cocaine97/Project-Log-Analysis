# Project  : Log Analysis
___
## Pre-requisite
* VM
* Vagrant
* newsdsata.sql
**Click [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) for a guide to setting up the pre-requisite for the project**
## Installation
* Download zip file or clone the repository to your local machine.
* Move the content of the downloaded file to the folder where your database ``
* Open your terminal and run command `vagrant up` followed by `vagrant ssh`
* Run `psql -d news`
* You're in the newsdata database now, run the following commands to create views required in order to run the queries in file **dfg.py**.
    * `create view dfg as select path,count(ip) as visits from log  where status = '200 OK' group by path order by visits desc offset 1;`
    * `create view art as select concat('/article/',slug) as path,title,author from articles;`
    * `create view queryOne as select title,author,visits from dfg join art on dfg.path=art.path;`
    * `create view queryTwo as select name,title,visits from authors join queryOne on authors.id = queryOne.author;`
    * `create view err as select time::timestamp::date as day,method,count(status) as error from log where status != '200 OK' group by day,method;`
    * `create view tot as select count(method) as total,time::timestamp::date as day from log group by day;`
    * `create view queryThree as select tot.day,total,error from tot join err on tot.day = err.day;`
* *Control-Z* from the psql command line.
* Run `python dfg.py`
* A Screenshot `output.png` of the program actually running in the terminal is in the zip file, along with a `output.txt` .
___



