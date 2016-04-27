"""
Write a script called "database.py" to print out the cities with the July being the warmest month. Your script must:
Connect to the database
Create the cities and weather tables (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)
Insert data into the two tables
Join the data together
Load into a pandas DataFrame
Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."
"""
import sqlite3 as lite
import pandas as pd

#Creating a tuple of city data
cities = (('New York City', 'NY'),
          ('Boston', 'MA'),
          ('Chicago', 'IL'),
          ('Miami', 'FL'),
          ('Dallas', 'TX'),
          ('Seattle', 'WA'),
          ('Portland', 'OR'),
          ('San Francisco', 'CA'),
          ('Los Angeles', 'CA'))

#Creating a tuple of weather data
weather = (('New York City', 2013, 'July', 'January', 62),
           ('Boston', 2013, 'July', 'January', 59),
           ('Chicago', 2013, 'July', 'January', 59),
           ('Miami', 2013, 'August', 'January', 84),
           ('Dallas', 2013, 'July', 'January', 77),
           ('Seattle', 2013, 'July', 'January', 61),
           ('Portland', 2013, 'July', 'December', 63),
           ('San Francisco', 2013, 'September', 'December', 64),
           ('Los Angeles', 2013, 'September', 'December', 75))

#Establishing connection with database
#Deleting tables if they exist
#Entering values of cities and tables into the database
#Query to pull out the data
con = lite.connect('challenge_database.db')
with con:
    cur = con.cursor()
    con.execute('DROP TABLE IF EXISTS cities')
    con.execute('DROP TABLE IF EXISTS weather')
    con.execute('CREATE TABLE cities(Name text, State text)')
    con.execute('CREATE TABLE weather(City text, Year integer, Warm_Month text, Cold_Month text, Average High integer)')
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    data = cur.execute("SELECT City,State FROM cities INNER JOIN weather ON name = city WHERE Warm_Month = 'July'")


#They query result is fetched and pushed into a data frame.
    rows = cur.fetchall()
    df = pd.DataFrame(rows)

#Printing the result in a single sentence using the while loop.
    print "The cities that are warmest in July are: ",
    counter = 0
    while counter < df.__len__():
        print df[0][counter]+' , '+df[1][counter]+' , ',
        counter += 1



