#%%
import datadotworld as dw
import altair as alt

# %%

# GQ 1) Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

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
print(gq1.dataframe.to_markdown())


# %%
# Grand Question 2: This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)

# %%
# 2.1) Write an SQL query that provides playerID, yearID, and batting average for players with at least 1 at bat that year. Sort the table from highest batting average to lowest, and then by playerid alphabetically. Show the top 5 results in your report.

gq2_1 = dw.query('byuidss/cse-250-baseball-database',
    """
    SELECT  playerID
          , yearID
        #   , h AS HHH
        #   , ab
          , (h / ab) AS batting_avg
    FROM batting
    WHERE (h / ab) > 0.5
    ORDER BY batting_avg DESC, playerID
    LIMIT 5
    """)
print(gq2_1.dataframe.to_markdown())


#%%
# 2.2) Use the same query as above, but only include players with at least 10 at bats that year. Print the top 5 results.

gq2_2 = dw.query('byuidss/cse-250-baseball-database',
    """
    SELECT  playerID
          , yearID
        #   , h 
        #   , ab
          , (h / ab) as batting_avg
    FROM batting
    WHERE ab >= 10
    ORDER BY batting_avg DESC, playerID
    LIMIT 5
    """)
print(gq2_2.dataframe.to_markdown())

# %%
# 2.3) Now calculate the batting average for players over their entire careers (all years combined). Only include players with at least 100 at bats, and print the top 5 results.

gq2_3 = dw.query('byuidss/cse-250-baseball-database',
    """
    SELECT playerid
         , (sum(h) / sum(ab)) as batting_avg
    FROM batting
    WHERE ab > 100
    GROUP BY playerid
    ORDER BY batting_avg DESC, playerid
    LIMIT 5
    """)
print(gq2_3.dataframe.to_markdown())

# %%
# Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc). Write an SQL query to get the data you need, then make a graph in Altair to visualize the comparison.

gq3 = dw.query('byuidss/cse-250-baseball-database',
    """
    SELECT name AS team
         , COUNT_IF(wswin = "Y") AS world_series_wins
    FROM teams
    WHERE name = "Boston Red Sox" OR name = "Chicago White Sox" 
    GROUP BY teamid
    """)
# gq3.dataframe
gq3_dat = gq3.dataframe

chart_3 = (
alt.Chart(gq3_dat)
.mark_bar()
.encode(x = alt.X('world_series_wins:Q', title = "World Series Wins"), 
        y = alt.Y('team:O', title = ""))

)
chart_3.save("gq_chart3.png")
# %%
