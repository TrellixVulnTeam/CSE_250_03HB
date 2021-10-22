#%%
import datadotworld as dw

#%%

results = dw.query('byuidss/cse-250-baseball-database', 
    """
    SELECT playerid, yearid, teamid, h, er, hr, bb, so
    FROM pitching
    WHERE yearid = 1874 and h > 405 and hr < 5
    ORDER BY hr 
    """)

print(results.dataframe)

#%%
# Select all columns from the batting table and limit the output to 2 rows. How many at bats did addybo01 have?
qr = dw.query('byuidss/cse-250-baseball-database', 
    """
    SELECT *
    FROM batting
    LIMIT 2

    """)
dat = (qr.dataframe)

# %%
