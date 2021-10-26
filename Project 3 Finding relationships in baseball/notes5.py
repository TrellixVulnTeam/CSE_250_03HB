#%%
import datadotworld as dw

# Don't use print to output the dataset. Just print it by stating itself. 

#%%

results = dw.query('byuidss/cse-250-baseball-database', 
    """
    SELECT playerid, yearid, teamid, h, er, hr, bb, so
    FROM pitching
    WHERE yearid = 1874 and h > 405 and hr < 5
    ORDER BY hr 
    """)

# print(results.dataframe)
results.dataframe

#%%
# Select all columns from the batting table and limit the output to 2 rows. How many at bats did addybo01 have?
qr = dw.query('byuidss/cse-250-baseball-database', 
    """
    SELECT *
    FROM batting
    LIMIT 2

    """)
dat = (qr.dataframe)
# print(dat)

# %%

# GQ 1) Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

gq1 = dw.query('byuidss/cse-250-baseball-database',
"""
SELECT playerID.collegeplaying,  
       yearID.collegeplaying, 
       salary.salaries,
       schoolID.collegeplaying,
       teamID.salaries
FROM CollegePlaying   
    LEFT JOIN playerID
    ON playerID.salaries = playerID.collegeplaying
""")
gq1.dataframe


# %%
gq1 = dw.query('byuidss/cse-250-baseball-database',
    """
    SELECT DISTINCT s.playerID AS PlayerID, 
                    schoolID AS SchoolID, 
                    s.salary AS Salary, 
                    s.yearID AS Year, 
                    s.teamid AS TeamID
    FROM salaries AS s
    JOIN collegeplaying AS cp
    ON s.playerID = cp.playerID
    WHERE cp.schoolid = "idbyuid"
    ORDER BY s.salary DESC
    """)
gq1.dataframe
# %%
# This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)

    #1. Write an SQL query that provides playerID, yearID, and batting average for players with at least 1 at bat that year. Sort the table from highest batting average to lowest, and then by playerid alphabetically. Show the top 5 results in your report.
    
    #2. Use the same query as above, but only include players with at least 10 at bats that year. Print the top 5 results.
    
    #3. Now calculate the batting average for players over their entire careers (all years combined). Only include players with at least 100 at bats, and print the top 5 results.

gq2 = dw.query('byuidss/cse-250-baseball-database',
    """
    SELECT playerID, sum(hr)/sum(h) AS AVG_Thing
    FROM batting
    GROUP BY playerid
    LIMIT 5
    """)
gq2.dataframe

#only add aliases for questions where those names are in the other table
#remember to explore the data using the select * from table