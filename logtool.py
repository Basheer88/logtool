#!/usr/bin/env python2
import psycopg2
import calendar

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


# Get the Top Three most viewed Articles of all time.
def getTopArticles():
    c.execute("""select articles.title, count(*) as num
                 from articles join log
                 on log.path like '%' || articles.slug
                 group by articles.title
                 order by num desc
                 limit 3;""")
    posts = c.fetchall()
    print "\n   The most three popular articles of all time   \n " + '=' * 48
    for pos in posts:
        print ' "' + pos[0]+'"-- ' + str(pos[1]) + ' views'


# Get the top most viewed Authors.
def getTopAuthors():
    c.execute("""select authors.name, sum(num) as total
                 from (articles join (select articles.title, count(*) as num
                                      from articles join log
                                      on log.path like '%' || articles.slug
                                      group by articles.title) as ccc
                 on articles.title = ccc.title) as BBB
                 join authors on BBB.author = authors.id
                 group by authors.name
                 order by total desc;""")
    posts = c.fetchall()
    print "\n  The most popular authors of all time \n " + '=' * 38
    for pos in posts:
        print ' ' + pos[0] + ' -- ' + str(pos[1]) + ' views'


# Get all days who have more than 1% error.
# A1 and A2 is a view please check README.md file to know more about them.
def getError():
    c.execute("""select A1.time, (trunc(100.0*(A1.er::decimal/A2.total), 1) ) as per
                 from A1 join A2
                 on A1.time = A2.time
                    and trunc(100.0*(A1.er::decimal/A2.total), 1) > 1.0;""")
    posts = c.fetchall()
    print "\n  Which Day have error more than 1% \n " + '=' * 35
    for pos in posts:
        x = str(pos[0]).split('-')
        month = '  ' + calendar.month_name[int(x[1])]
        day = ' ' + x[2] + ','
        year = ' ' + x[0]
        percent = str(pos[1])
        print month + day + year + ' -- ' + percent + '% errors'

getTopArticles()
getTopAuthors()
getError()
db.close()
