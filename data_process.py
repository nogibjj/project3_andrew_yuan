import sqlite3

conn = sqlite3.connect("covid.db")
cursor = conn.cursor

# three options to choose

# choice 1 : fetch the data of one country
cmd1 = """
    SELECT 




"""


# choice 2 : sort the countries by either total_cases or total_deaths



# choice 3: calculate the death-infection rate of each country and sort


if __name__ == 'main':
    