#!/usr/bin/env python
import psycopg2


queryOne = 'select title, visits from queryOne  limit 3'
queryTwo = ('select name,sum(visits) as views from queryTwo group'
            ' by name order by views desc limit 3;')
queryThree = ('select day,error*100.00/total as percent_error from '
              'queryThree where error*100/total> 1;')


def print_em_up(query):
    for x in query:
        print x[0], ' ', x[1]
    print '\n\n'

db = psycopg2.connect('dbname=news')
c = db.cursor()

c.execute(queryOne)
q1 = c.fetchall()
print_em_up(q1)

c.execute(queryTwo)
q2 = c.fetchall()
print_em_up(q2)

c.execute(queryThree)
q3 = c.fetchall()
print_em_up(q3)
db.close()
